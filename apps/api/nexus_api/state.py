from packages.graph.identity_graph import OrgGraph
from packages.workflows.workflows_engine import WorkflowEngine


class AppState:
    def __init__(self):
        self.graph = OrgGraph()
        self.workflows = WorkflowEngine(self.graph)


state = AppState()
if not state.graph.snapshot()['nodes']:
    ceo = state.graph.add_node('EMPLOYEE', 'Sarah', {'role': 'CEO', 'department': 'Executive'})
    for i in range(10):
        role = 'Software Engineer' if i % 2 == 0 else 'Sales Rep'
        dept = 'Engineering' if i % 2 == 0 else 'Sales'
        emp = state.graph.add_node('EMPLOYEE', f'Employee {i}', {'role': role, 'department': dept})
        state.graph.add_edge(emp, ceo, 'REPORTS_TO', {})
        state.workflows.handle_event('EMPLOYEE_CREATED', emp)
