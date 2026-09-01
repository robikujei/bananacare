import unittest

from bananacare import create_app, db
from bananacare.models import Assistance, DiseaseReport, FarmerProfile, User


class BananaCareTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app({
            "TESTING": True,
            "SECRET_KEY": "test",
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        })
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            admin = User(username="admin", role="admin")
            admin.set_password("admin123")
            farmer = User(username="farmer", role="farmer")
            farmer.set_password("farmer123")
            farmer.profile = FarmerProfile(full_name="Test Farmer", contact_number="09000000000",
                location="Test Area", farm_size=2, banana_variety="Cavendish")
            db.session.add_all([admin, farmer])
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def login_farmer(self):
        return self.client.post("/farmer/login", data={"username": "farmer", "password": "farmer123"}, follow_redirects=True)

    def test_valid_farmer_login(self):
        response = self.login_farmer()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, Test Farmer", response.data)

    def test_invalid_login_shows_error(self):
        response = self.client.post("/admin/login", data={"username": "admin", "password": "wrong"}, follow_redirects=True)
        self.assertIn(b"Invalid username, password, or account type", response.data)

    def test_valid_condition_report_is_saved(self):
        self.login_farmer()
        response = self.client.post("/farmer/reports/new", data={"problem_type": "Sigatoka", "affected_area": "0.5", "description": "Leaf spots observed"}, follow_redirects=True)
        self.assertIn(b"Farm condition report submitted", response.data)
        with self.app.app_context():
            self.assertEqual(DiseaseReport.query.count(), 1)

    def test_affected_area_cannot_exceed_farm_size(self):
        self.login_farmer()
        response = self.client.post("/farmer/reports/new", data={"problem_type": "Other", "affected_area": "3", "description": "Invalid edge case"}, follow_redirects=True)
        self.assertIn(b"cannot exceed farm size", response.data)
        with self.app.app_context():
            self.assertEqual(DiseaseReport.query.count(), 0)

    def test_farmer_cannot_open_admin_dashboard(self):
        self.login_farmer()
        response = self.client.get("/admin/dashboard")
        self.assertEqual(response.status_code, 403)

    def test_admin_dashboard_renders(self):
        response = self.client.post("/admin/login", data={"username": "admin", "password": "admin123"}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Monitoring overview", response.data)
        self.assertIn(b"Test Farmer", response.data)

    def test_assistance_request_is_saved(self):
        self.login_farmer()
        self.client.post("/farmer/assistance/new", data={"assistance_type": "Farm Visit", "recommendation": "Please inspect crops"})
        with self.app.app_context():
            self.assertEqual(Assistance.query.count(), 1)


if __name__ == "__main__":
    unittest.main()
