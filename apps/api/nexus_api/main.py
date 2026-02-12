from __future__ import annotations

from typing import Any

from apps.api.nexus_api.state import state


def healthz() -> dict[str, str]:
    return {'status': 'ok'}


def readyz() -> dict[str, str]:
    return {'status': 'ready'}


def get_graph() -> dict[str, Any]:
    return state.graph.snapshot()


def query(payload: dict[str, Any]) -> dict[str, Any]:
    return state.graph.run_query(payload)


def hire(name: str, role: str, department: str, manager_id: str | None = None) -> dict[str, Any]:
    employee_id = state.graph.add_node('EMPLOYEE', name, {'role': role, 'department': department})
    if manager_id:
        state.graph.add_edge(employee_id, manager_id, 'REPORTS_TO', {})
    wf = state.workflows.handle_event('EMPLOYEE_CREATED', employee_id)
    return {'employee_id': employee_id, 'workflow': wf}
