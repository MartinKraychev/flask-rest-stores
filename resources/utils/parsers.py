from flask_restful import reqparse

store_parser = reqparse.RequestParser()
store_parser.add_argument('name',
                          type=str,
                          required=True,
                          help="This field cannot be left blank!"
                          )

item_parser = reqparse.RequestParser()
item_parser.add_argument('name',
                         type=str,
                         required=True,
                         help="This field cannot be left blank!"
                         )
item_parser.add_argument('price',
                         type=float,
                         required=True,
                         help="This field cannot be left blank!"
                         )
item_parser.add_argument('store_id',
                         type=int,
                         required=True,
                         help="Every item must have a store"
                         )
