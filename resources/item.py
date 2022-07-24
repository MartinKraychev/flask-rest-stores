from flask_jwt import jwt_required
from flask_restful import Resource, marshal_with, marshal

from models.item import ItemModel
from resources.parsers import item_parser
from resources.resource_fieds import item_resource_fields


class Item(Resource):

    def get(self, item_id):
        item = ItemModel.find_by_id(item_id)
        if not item:
            return {'message': 'Item not found'}, 404
        return marshal(item, item_resource_fields)

    @jwt_required()
    def delete(self, item_id):
        item = ItemModel.find_by_id(item_id)
        if not item:
            return {'message': 'Item does not exist'}, 404

        item.delete_from_db()

        return {'message': 'Item deleted'}, 204

    @jwt_required()
    def put(self, item_id):
        item = ItemModel.find_by_id(item_id)
        if not item:
            return {"message": "Item not found"}, 404

        data = item_parser.parse_args()
        item.price = data['price']
        item.store_id = data['store_id']
        item.name = data['name']
        item.save_to_db()
        return marshal(item, item_resource_fields), 201


class ItemList(Resource):

    @marshal_with(item_resource_fields)
    def get(self):
        return ItemModel.query.all(), 200

    @jwt_required()
    def post(self):
        data = item_parser.parse_args()
        if ItemModel.find_by_name(data['name']):
            return {'message': f"An item with name {data['name']} already exists."}, 400

        item = ItemModel(**data)
        item.save_to_db()

        return marshal(item, item_resource_fields), 201
