import unittest
from pathlib import Path

from packages.graph.identity_graph import OrgGraph


class GraphTests(unittest.TestCase):
    def test_cycle_detection_blocks_edge(self):
        graph = OrgGraph(str(Path('tmp_graph1.db')))
        a = graph.add_node('EMPLOYEE', 'A', {'role': 'Software Engineer'})
        b = graph.add_node('EMPLOYEE', 'B', {'role': 'Software Engineer'})
        c = graph.add_node('EMPLOYEE', 'C', {'role': 'Software Engineer'})
        graph.add_edge(b, a, 'REPORTS_TO', {})
        graph.add_edge(c, b, 'REPORTS_TO', {})
        with self.assertRaises(ValueError):
            graph.add_edge(a, c, 'REPORTS_TO', {})

    def test_manager_termination_repair(self):
        graph = OrgGraph(str(Path('tmp_graph2.db')))
        ceo = graph.add_node('EMPLOYEE', 'CEO', {})
        mgr = graph.add_node('EMPLOYEE', 'Mgr', {})
        rep = graph.add_node('EMPLOYEE', 'Rep', {})
        graph.add_edge(mgr, ceo, 'REPORTS_TO', {})
        graph.add_edge(rep, mgr, 'REPORTS_TO', {})
        result = graph.repair_on_manager_termination(mgr)
        self.assertEqual(result['reassigned_to'], ceo)
        self.assertIn(ceo, graph.get_manager_chain(rep))

if __name__ == '__main__':
    unittest.main()
