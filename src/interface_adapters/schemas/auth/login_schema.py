from marshmallow import fields, validate


login_schema = {
    'email': fields.Str(validate=validate.Length(min=1), max=320, required=True),
    'password': fields.Str(validate=validate.Length(min=6, max=100), required=True)
}
