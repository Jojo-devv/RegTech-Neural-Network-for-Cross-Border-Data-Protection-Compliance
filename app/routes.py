from flask import jsonify, request
from app import app, db
from models import ComplianceRecord

@app.route('/compliance', methods=['GET'])
def get_compliance_records():
    records = ComplianceRecord.query.all()
    return jsonify([{'id': r.id, 'regulation': r.regulation, 'status': r.status} for r in records])

@app.route('/compliance', methods=['POST'])
def add_compliance_record():
    data = request.json
    new_record = ComplianceRecord(regulation=data['regulation'], status=data['status'])
    db.session.add(new_record)
    db.session.commit()
    return jsonify({'id': new_record.id}), 201

@app.route('/compliance/<int:id>', methods=['GET'])
def get_compliance_record(id):
    record = ComplianceRecord.query.get_or_404(id)
    return jsonify({'id': record.id, 'regulation': record.regulation, 'status': record.status})

@app.route('/compliance/<int:id>', methods=['PUT'])
def update_compliance_record(id):
    record = ComplianceRecord.query.get_or_404(id)
    data = request.json
    record.regulation = data['regulation']
    record.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Record updated successfully'})

@app.route('/compliance/<int:id>', methods=['DELETE'])
def delete_compliance_record(id):
    record = ComplianceRecord.query.get_or_404(id)
    db.session.delete(record)
    db.session.commit()
    return jsonify({'message': 'Record deleted successfully'})
