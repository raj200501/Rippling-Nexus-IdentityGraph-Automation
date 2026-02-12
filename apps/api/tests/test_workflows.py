import unittest
from pathlib import Path

from packages.graph.identity_graph import OrgGraph
from packages.workflows.workflows_engine import WorkflowEngine


class WorkflowTests(unittest.TestCase):
    def test_workflow_idempotent_access_and_device(self):
        graph = OrgGraph(str(Path('tmp_workflow1.db')))
        emp = graph.add_node('EMPLOYEE', 'Ana', {'department': 'Engineering', 'role': 'Software Engineer'})
        engine = WorkflowEngine(graph)
        first = engine.handle_event('EMPLOYEE_CREATED', emp)
        second = engine.handle_event('EMPLOYEE_UPDATED', emp)
        self.assertEqual(first['status'], 'success')
        self.assertTrue(any(step['status'] == 'noop' for step in second['steps']))

    def test_integration_retry_deterministic(self):
        graph = OrgGraph(str(Path('tmp_workflow2.db')))
        emp = graph.add_node('EMPLOYEE', 'Bob', {'department': 'Engineering', 'role': 'Engineer'})
        engine = WorkflowEngine(graph)
        engine.integrations['github'].failure_rate = 1.0
        run = engine.handle_event('EMPLOYEE_CREATED', emp)
        step = next(s for s in run['steps'] if s['action'] == 'ensure_access')
        self.assertFalse(step['result']['ok'])
        self.assertEqual(step['result']['retries'], 3)

if __name__ == '__main__':
    unittest.main()
