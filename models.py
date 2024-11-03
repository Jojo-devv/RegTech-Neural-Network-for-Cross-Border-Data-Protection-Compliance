from flask_sqlalchemy import SQLAlchemy

# Initialize the database instance
db = SQLAlchemy()

# Define the ComplianceRecord model
class ComplianceRecord(db.Model):
    __tablename__ = 'compliance_records'  # Name of the database table
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    regulation = db.Column(db.String(255), nullable=False)  # Name of the regulation
    status = db.Column(db.String(50), nullable=False)  # Compliance status
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())  # Timestamp of creation

    def __repr__(self):
        return f'<ComplianceRecord {self.regulation}: {self.status} (ID: {self.id})>'

# Define the User model (for future user management)
class User(db.Model):
    __tablename__ = 'users'  # Name of the user table
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    username = db.Column(db.String(50), unique=True, nullable=False)  # Unique username
    password_hash = db.Column(db.String(128), nullable=False)  # Hashed password
    email = db.Column(db.String(120), unique=True, nullable=False)  # Unique email
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())  # Timestamp of account creation

    def __repr__(self):
        return f'<User {self.username} (ID: {self.id})>'

