from marshmallow import fields, validate

register_schema = {
    'email': fields.Str(validate=validate.Length(min=1), max=320, required=True),
    'password': fields.Str(validate=validate.Length(min=6, max=100), required=True),
    'first_name': fields.Str(),
    'last_name': fields.Str()
}