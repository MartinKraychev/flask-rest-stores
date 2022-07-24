from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.store import StoreList, Store
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from db import db

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.secret_key = 'jose'
api = Api(app)

app.config['JWT_AUTH_URL_RULE'] = '/login'
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<int:item_id>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(StoreList, '/stores')
api.add_resource(Store, '/store/<int:store_id>')


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
