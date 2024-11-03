import unittest
import json
from app import app, db, ComplianceRecord

class ComplianceAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Create a temporary database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_compliance_records(self):
        response = self.app.get('/compliance')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), [])

    def test_add_compliance_record(self):
        response = self.app.post('/compliance', json={'regulation': 'GDPR', 'status': 'Compliant'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', json.loads(response.data))

    def test_get_compliance_record(self):
        self.app.post('/compliance', json={'regulation': 'GDPR', 'status': 'Compliant'})
        response = self.app.get('/compliance/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('regulation', json.loads(response.data))

    def test_update_compliance_record(self):
        self.app.post('/compliance', json={'regulation': 'GDPR', 'status': 'Compliant'})
        response = self.app.put('/compliance/1', json={'regulation': 'GDPR', 'status': 'Non-compliant'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['message'], 'Record updated successfully')

    def test_delete_compliance_record(self):
        self.app.post('/compliance', json={'regulation': 'GDPR', 'status': 'Compliant'})
        response = self.app.delete('/compliance/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['message'], 'Record deleted successfully')

if __name__ == '__main__':
    unittest.main()
