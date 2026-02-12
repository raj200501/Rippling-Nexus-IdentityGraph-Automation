from __future__ import annotations

from typing import Any

from packages.integrations.mock_integrations.adapters import MockGitHub, MockOkta


class WorkflowEngine:
    def __init__(self, graph):
        self.graph = graph
        self.integrations = {'github': MockGitHub(), 'okta': MockOkta()}

    def handle_event(self, event_type: str, employee_id: str, dry_run: bool = False) -> dict[str, Any]:
        snapshot = self.graph.snapshot()
        employee = next((n for n in snapshot['nodes'] if n['id'] == employee_id), None)
        if not employee:
            return {'status': 'failed', 'steps': []}
        event_id = self.graph.log_event(event_type, {'employee_id': employee_id})
        steps=[]
        attrs=employee.get('attrs', {})
        if event_type in {'EMPLOYEE_CREATED', 'EMPLOYEE_UPDATED'}:
            if attrs.get('department') == 'Engineering' or 'Engineer' in attrs.get('role', ''):
                steps += self._ensure_access(employee, 'GitHub', dry_run)
                steps += self._ensure_device(employee, 'MacBook Pro', dry_run)
            if attrs.get('department') == 'Sales':
                steps += self._ensure_access(employee, 'Salesforce', dry_run)
                steps += self._ensure_device(employee, 'Windows Laptop', dry_run)
        if event_type == 'EMPLOYEE_TERMINATED':
            steps += self._revoke_access(employee, dry_run)
        rid=self.graph.create_workflow_run(event_id, 'dry-run' if dry_run else 'success', {'steps':steps})
        return {'run_id':rid, 'status':'dry-run' if dry_run else 'success', 'steps':steps}

    def _ensure_access(self, employee: dict[str, Any], app_name: str, dry_run: bool) -> list[dict[str, Any]]:
        snap=self.graph.snapshot()
        app=next((n for n in snap['nodes'] if n['kind']=='APPLICATION' and n['display_name']==app_name), None)
        app_id=app['id'] if app else self.graph.add_node('APPLICATION', app_name, {})
        exists=any(e['kind']=='HAS_ACCESS_TO' and e['src']==employee['id'] and e['dst']==app_id for e in snap['edges'])
        if exists: return [{'action':'ensure_access','status':'noop','app':app_name}]
        if dry_run: return [{'action':'ensure_access','status':'would_grant','app':app_name}]
        result=self.integrations['github'].provision_access({'id':employee['id']}, app_name)
        self.graph.add_edge(employee['id'], app_id, 'HAS_ACCESS_TO', {'source':'rule'})
        return [{'action':'ensure_access','status':'granted','app':app_name,'result':result}]

    def _ensure_device(self, employee: dict[str, Any], device_type: str, dry_run: bool) -> list[dict[str, Any]]:
        snap=self.graph.snapshot()
        exists=any(e['kind']=='ASSIGNED_TO' and e['dst']==employee['id'] for e in snap['edges'])
        if exists: return [{'action':'ensure_device','status':'noop'}]
        if dry_run: return [{'action':'ensure_device','status':'would_assign'}]
        device=self.graph.add_node('DEVICE', device_type, {'status':'assigned'})
        self.graph.add_edge(device, employee['id'], 'ASSIGNED_TO', {'source':'rule'})
        result=self.integrations['okta'].provision_device({'id':employee['id']}, device_type)
        return [{'action':'ensure_device','status':'assigned','result':result}]

    def _revoke_access(self, employee: dict[str, Any], dry_run: bool) -> list[dict[str, Any]]:
        snap=self.graph.snapshot(); steps=[]
        for edge in [e for e in snap['edges'] if e['kind']=='HAS_ACCESS_TO' and e['src']==employee['id']]:
            if dry_run:
                steps.append({'action':'revoke','status':'would_revoke'})
            else:
                self.graph.conn.execute('DELETE FROM edges WHERE id=?', (edge['id'],)); self.graph.conn.commit()
                steps.append({'action':'revoke','status':'revoked'})
        return steps
