from marshmallow import fields

register_schema = {
    'email': fields.Str(),
    'password': fields.Str(),
    'first_name': fields.Str(),
    'last_name': fields.Str()
}
