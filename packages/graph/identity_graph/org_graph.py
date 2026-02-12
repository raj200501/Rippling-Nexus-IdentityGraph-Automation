from __future__ import annotations

import uuid
from typing import Any

from packages.graph.identity_graph.query import execute_query
from packages.graph.identity_graph.storage import connect, dump_json, load_json, now_ts


class OrgGraph:
    def __init__(self, db_path: str = './.nexus/state.db') -> None:
        self.conn = connect(db_path)

    def add_node(self, kind: str, display_name: str, attrs: dict[str, Any] | None = None, node_id: str | None = None) -> str:
        nid = node_id or f"node_{uuid.uuid4().hex[:12]}"
        self.conn.execute('INSERT OR REPLACE INTO nodes(id, kind, display_name, attrs_json, created_at) VALUES(?,?,?,?,?)', (nid, kind, display_name, dump_json(attrs or {}), now_ts()))
        self.conn.commit()
        return nid

    def add_edge(self, src: str, dst: str, kind: str, attrs: dict[str, Any] | None = None, edge_id: str | None = None) -> str:
        if kind == 'REPORTS_TO':
            self.validate_no_cycle_on_new_edge(src, dst)
        eid = edge_id or f"edge_{uuid.uuid4().hex[:12]}"
        self.conn.execute('INSERT OR REPLACE INTO edges(id, src, dst, kind, attrs_json, created_at) VALUES(?,?,?,?,?,?)', (eid, src, dst, kind, dump_json(attrs or {}), now_ts()))
        self.conn.commit()
        return eid

    def snapshot(self) -> dict[str, Any]:
        nodes = [dict(row) | {'attrs': load_json(row['attrs_json'])} for row in self.conn.execute('SELECT * FROM nodes')]
        edges = [dict(row) | {'attrs': load_json(row['attrs_json'])} for row in self.conn.execute('SELECT * FROM edges')]
        for n in nodes:
            n.pop('attrs_json', None); n.pop('created_at', None)
        for e in edges:
            e.pop('attrs_json', None); e.pop('created_at', None)
        return {'nodes': nodes, 'edges': edges}

    def _manager_of(self, employee_id: str) -> str | None:
        row = self.conn.execute("SELECT dst FROM edges WHERE src=? AND kind='REPORTS_TO' LIMIT 1", (employee_id,)).fetchone()
        return row['dst'] if row else None

    def get_manager_chain(self, employee_id: str) -> list[str]:
        chain=[]; seen=set(); cur=employee_id
        while cur not in seen:
            seen.add(cur)
            mgr=self._manager_of(cur)
            if not mgr: break
            chain.append(mgr); cur=mgr
        return chain

    def get_reports(self, manager_employee_id: str, depth: int | None = None) -> list[str]:
        reports=[]; frontier=[(manager_employee_id,0)]
        while frontier:
            mgr,d=frontier.pop(0)
            if depth is not None and d>=depth: continue
            for row in self.conn.execute("SELECT src FROM edges WHERE dst=? AND kind='REPORTS_TO'", (mgr,)):
                reports.append(row['src']); frontier.append((row['src'], d+1))
        return reports

    def detect_cycles(self) -> list[list[str]]:
        cycles=[]
        for node in [r['id'] for r in self.conn.execute("SELECT id FROM nodes WHERE kind='EMPLOYEE'")]:
            chain=self.get_manager_chain(node)
            if len(chain)!=len(set(chain)):
                cycles.append(chain)
        return cycles

    def validate_no_cycle_on_new_edge(self, src: str, dst: str) -> None:
        chain=self.get_manager_chain(dst)
        if src==dst or src in chain:
            raise ValueError('REPORTS_TO edge would create cycle')

    def repair_on_manager_termination(self, manager_id: str) -> dict[str, Any]:
        upper=self._manager_of(manager_id)
        reports=[r['src'] for r in self.conn.execute("SELECT src FROM edges WHERE dst=? AND kind='REPORTS_TO'", (manager_id,))]
        self.conn.execute("DELETE FROM edges WHERE dst=? AND kind='REPORTS_TO'", (manager_id,))
        if upper:
            for rep in reports:
                self.add_edge(rep, upper, 'REPORTS_TO', {'repaired': True})
        self.conn.commit()
        return {'reassigned_to': upper, 'reports': reports}

    def run_query(self, query: dict[str, Any]) -> dict[str, Any]:
        return execute_query(self.snapshot(), query)

    def log_event(self, event_type: str, payload: dict[str, Any]) -> str:
        eid=f"evt_{uuid.uuid4().hex[:12]}"
        self.conn.execute('INSERT INTO events(id, ts, type, payload_json) VALUES(?,?,?,?)', (eid, now_ts(), event_type, dump_json(payload))); self.conn.commit(); return eid

    def log_audit(self, message: str, level: str = 'INFO', context: dict[str, Any] | None = None) -> str:
        aid=f"aud_{uuid.uuid4().hex[:12]}"
        self.conn.execute('INSERT INTO audit_log(id, ts, level, message, context_json) VALUES(?,?,?,?,?)', (aid, now_ts(), level, message, dump_json(context or {}))); self.conn.commit(); return aid

    def list_audit(self, limit: int = 200) -> list[dict[str, Any]]:
        return [dict(r)|{'context':load_json(r['context_json'])} for r in self.conn.execute('SELECT * FROM audit_log ORDER BY ts DESC LIMIT ?', (limit,))]

    def list_events(self, limit: int = 200) -> list[dict[str, Any]]:
        return [dict(r)|{'payload':load_json(r['payload_json'])} for r in self.conn.execute('SELECT * FROM events ORDER BY ts DESC LIMIT ?', (limit,))]

    def create_workflow_run(self, event_id: str, status: str, details: dict[str, Any]) -> str:
        rid=f"wfr_{uuid.uuid4().hex[:12]}"
        self.conn.execute('INSERT INTO workflow_runs(id, ts, event_id, status, details_json) VALUES(?,?,?,?,?)', (rid, now_ts(), event_id, status, dump_json(details))); self.conn.commit(); return rid

    def list_workflow_runs(self) -> list[dict[str, Any]]:
        return [dict(r)|{'details':load_json(r['details_json'])} for r in self.conn.execute('SELECT * FROM workflow_runs ORDER BY ts DESC LIMIT 500')]
