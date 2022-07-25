import os

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.store import StoreList, Store
from resources.user import UserRegister, User, UserLogin
from resources.item import Item, ItemList
from db import db


uri = os.getenv("DATABASE_URL", 'sqlite:///db.sqlite3')
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.secret_key = 'jose'
api = Api(app)

jwt = JWTManager(app)


api.add_resource(Item, '/item/<int:item_id>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(StoreList, '/stores')
api.add_resource(Store, '/store/<int:store_id>')
api.add_resource(User, '/users/<int:user_id>')


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
