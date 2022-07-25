from flask_restful import fields


item_resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'price': fields.Float,
    'store_id': fields.Integer
}

store_resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'items': fields.Nested(item_resource_fields)
}

user_resource_fields = {
    'id': fields.Integer,
    'username': fields.String
}
