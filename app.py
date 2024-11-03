from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import yaml
import logging

# Initialize the Flask application
app = Flask(__name__)

# Load configuration from config.yaml
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{config['database']['user']}:{config['database']['password']}@{config['database']['host']}:{config['database']['port']}/{config['database']['db_name']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(filename=config['logging']['log_file'], level=config['logging']['level'], format='%(asctime)s - %(levelname)s - %(message)s')

# Define a sample model for compliance records
class ComplianceRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    regulation = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<ComplianceRecord {self.regulation}: {self.status}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to check the health of the application
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "Healthy"}), 200

# Route to add a new compliance record
@app.route('/compliance', methods=['POST'])
def add_compliance():
    data = request.json
    new_record = ComplianceRecord(regulation=data['regulation'], status=data['status'])
    db.session.add(new_record)
    db.session.commit()
    logging.info(f'Added compliance record: {new_record}')
    return jsonify({"message": "Compliance record added successfully!"}), 201

# Route to get all compliance records
@app.route('/compliance', methods=['GET'])
def get_compliance_records():
    records = ComplianceRecord.query.all()
    return jsonify([{"id": record.id, "regulation": record.regulation, "status": record.status} for record in records]), 200

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
