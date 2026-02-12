from __future__ import annotations

from typing import Any


def execute_query(snapshot: dict[str, Any], query: dict[str, Any]) -> dict[str, Any]:
    nodes = {node['id']: node for node in snapshot['nodes']}
    edges = snapshot['edges']
    where = query.get('where', {})
    constraints = query.get('constraints', [])
    employees = [n for n in snapshot['nodes'] if n.get('kind') == 'EMPLOYEE']
    matches = []
    explanations: dict[str, list[str]] = {}

    for emp in employees:
        attrs = emp.get('attrs', {})
        if any(attrs.get(k) != v for k, v in where.items()):
            continue
        ok = True
        reasons: list[str] = []
        for constraint in constraints:
            if constraint.get('type') == 'REPORTS_TO':
                if not _reports_to(emp['id'], constraint.get('manager_name'), nodes, edges, constraint.get('mode', 'direct')):
                    ok = False
                    break
                reasons.append('reports_to')
            if constraint.get('type') == 'HAS_ACCESS_TO':
                if not _has_access(emp['id'], constraint.get('app'), nodes, edges):
                    ok = False
                    break
                reasons.append('has_access')
        if ok:
            matches.append(emp)
            explanations[emp['id']] = reasons
    return {'employees': matches, 'explanations': explanations, 'count': len(matches)}


def _reports_to(employee_id: str, manager_name: str, nodes: dict[str, Any], edges: list[dict[str, Any]], mode: str) -> bool:
    managers = [n['id'] for n in nodes.values() if n.get('display_name') == manager_name]
    if not managers:
        return False
    target = managers[0]
    if mode == 'direct':
        return any(e['kind'] == 'REPORTS_TO' and e['src'] == employee_id and e['dst'] == target for e in edges)
    seen = set()
    cur = employee_id
    while cur not in seen:
        seen.add(cur)
        relation = next((e for e in edges if e['kind'] == 'REPORTS_TO' and e['src'] == cur), None)
        if relation is None:
            return False
        if relation['dst'] == target:
            return True
        cur = relation['dst']
    return False


def _has_access(employee_id: str, app_name: str, nodes: dict[str, Any], edges: list[dict[str, Any]]) -> bool:
    app_ids = {n['id'] for n in nodes.values() if n.get('display_name') == app_name and n.get('kind') == 'APPLICATION'}
    return any(e['kind'] == 'HAS_ACCESS_TO' and e['src'] == employee_id and e['dst'] in app_ids for e in edges)
