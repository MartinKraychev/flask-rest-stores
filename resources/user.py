from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required
from flask_restful import Resource, reqparse, marshal

from models.user import UserModel
from resources.utils.resource_fieds import user_resource_fields
from hmac import compare_digest

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username',
                    type=str,
                    required=True,
                    help="This field cannot be left blank!"
                    )
_user_parser.add_argument('password',
                    type=str,
                    required=True,
                    help="This field cannot be left blank!"
                    )


class UserRegister(Resource):

    def post(self):
        data = _user_parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User with that username already exists."}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201


class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': "User not found."}, 404

        return marshal(user, user_resource_fields), 200

    @classmethod
    @jwt_required()
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': "User not found."}, 404

        user.delete_from_db()
        return {'message': 'User deleted'}, 200


class UserLogin(Resource):
    @classmethod
    def post(cls):
        data = _user_parser.parse_args()

        # Replaces the security package
        user = UserModel.find_by_username(data['username'])
        if user and compare_digest(user.password, data['password']):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)

            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        else:
            return {'message': 'Invalid credentials'}, 401
