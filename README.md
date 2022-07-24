# Flask Rest Application witj JWT token containing users, stores and items.

## Api Endpoints:
  - Auth:
    - POST -> http://127.0.0.1:5000/register
    - POST ->  http://127.0.0.1:5000/login
   
  - Stores:
    - GET ->  http://127.0.0.1:5000/stores
    - POST ->  http://127.0.0.1:5000/stores
    - GET ->  http://127.0.0.1:5000/store/{id}
    - PUT -> http://127.0.0.1:5000/store/{id}
    - DELETE -> http://127.0.0.1:5000/store/{id}
  
  - Items:
    - GET -> http://127.0.0.1:5000/items
    - POST -> http://127.0.0.1:5000/items
    - GET -> http://127.0.0.1:5000/item/{id}
    - PUT -> http://127.0.0.1:5000/item/{id}
    - DELETE -> http://127.0.0.1:5000/item/{id}
