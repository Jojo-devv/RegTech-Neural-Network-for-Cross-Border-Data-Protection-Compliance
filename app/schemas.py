from marshmallow import Schema, fields

class ComplianceRecordSchema(Schema):
    id = fields.Int(dump_only=True)
    regulation = fields.Str(required=True)
    status = fields.Str(required=True)
