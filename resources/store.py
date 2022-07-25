from flask_jwt_extended import jwt_required
from flask_restful import Resource, marshal_with, marshal

from models.store import StoreModel
from resources.utils.parsers import store_parser
from resources.utils.resource_fieds import store_resource_fields


class Store(Resource):

    def get(self, store_id):
        store = StoreModel.find_by_id(store_id)
        if not store:
            return {'message': 'store not found'}, 404

        return marshal(store, store_resource_fields), 200

    @jwt_required()
    def delete(self, store_id):
        store = StoreModel.find_by_id(store_id)
        if not store:
            return {'message': 'store not found'}, 404

        store.delete_from_db()
        return {'message': 'store deleted'}, 200

    @jwt_required()
    def put(self, store_id):
        store = StoreModel.find_by_id(store_id)
        if not store:
            return {"message": "Item not found"}, 404

        data = store_parser.parse_args()
        store.name = data['name']
        store.save_to_db()

        return marshal(store, store_resource_fields), 201


class StoreList(Resource):

    @marshal_with(store_resource_fields)
    def get(self):
        return StoreModel.query.all(), 200

    @jwt_required()
    def post(self):
        data = store_parser.parse_args()
        if StoreModel.find_by_name(data['name']):
            return {'message': f"An store with name {data['name']} already exists."}, 400

        store = StoreModel(**data)
        store.save_to_db()
        return marshal(store, store_resource_fields), 201
