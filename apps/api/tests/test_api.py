import unittest

from apps.api.nexus_api.main import healthz, query


class ApiTests(unittest.TestCase):
    def test_healthz(self):
        self.assertEqual(healthz()['status'], 'ok')

    def test_query_contract(self):
        payload = {
            'select': 'EMPLOYEE',
            'where': {'role': 'Software Engineer'},
            'constraints': [
                {'type': 'REPORTS_TO', 'manager_name': 'Sarah', 'mode': 'transitive'},
                {'type': 'HAS_ACCESS_TO', 'app': 'GitHub'},
            ],
        }
        body = query(payload)
        self.assertIn('employees', body)

if __name__ == '__main__':
    unittest.main()
