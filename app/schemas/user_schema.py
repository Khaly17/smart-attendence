from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    badge_id = fields.Str(required=True)
    role = fields.Str()
