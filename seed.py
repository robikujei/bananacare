from bananacare import create_app, db
from bananacare.constants import ADMIN_ROLE, FARMER_ROLE
from bananacare.models import Assistance, DiseaseReport, FarmerProfile, User

app = create_app()
with app.app_context():
    if not User.query.filter_by(username="admin").first():
        admin = User(username="admin", role=ADMIN_ROLE)
        admin.set_password("admin123")
        db.session.add(admin)
    if not User.query.filter_by(username="farmer1").first():
        farmer = User(username="farmer1", role=FARMER_ROLE)
        farmer.set_password("farmer123")
        farmer.profile = FarmerProfile(full_name="Juan Dela Cruz", contact_number="09123456789",
            location="Sample Farm Area", farm_size=2.5, banana_variety="Cavendish")
        db.session.add(farmer)
        db.session.flush()
        db.session.add(DiseaseReport(farmer_id=farmer.profile.id, problem_type="Sigatoka",
            affected_area=0.4, description="Dark spots observed on several leaves."))
        db.session.add(Assistance(farmer_id=farmer.profile.id, assistance_type="Farm Visit",
            recommendation="Requesting inspection and disease-control advice."))
    db.session.commit()
    print("Demo data ready. Admin: admin/admin123 | Farmer: farmer1/farmer123")
