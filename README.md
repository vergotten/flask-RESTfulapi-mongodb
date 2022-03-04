# **Flask-restfulapi-mongodb**

Microservice for e-shop <br />
Model/entities: <br />
- Products - is responsible for the goods in the warehouse, <br />
for example - a phone with a name and manufacturer. <br />

Fields: <br />
- identifier (ID) <br />
- title <br />
- description <br />
- parameters: array of key/value pairs <br />

Libraries used in this project: <br />
- flask <br />
- pymongo <br />

Entities are stored in MongoDB at localhost:27017 <br />

To install dependencies and libraries use following command: <br />
`pip install -r requirements.txt` <br />

To launch mongodb in docker use: <br />
`docker run -d -p 27017:27017 mongo` <br />

REST API methods: <br />
- Create a new product <br />
- Get a list of product names, with the ability to filter by: <br />

- a) name <br />
- b) the selected parameter and its value <br />
- Get product details by ID <br />

Methods accept JSON as input and return JSON as output. <br />

To launch application use: <br /> 
`python app.py` <br />

# Curl commands: <br />

json product files are stored in curl_requests/products folder. <br />
Json requests are presented in the form: <br />

`{
    "database": "ProductsDB",
    "collection": "products",
    "Filter" : {
        "description" : "Smartphone"
    }
}`

to add a single product use curl: <br />
`curl -X POST localhost:5000/productsdb -H 'Content-Type: application/json' -d @curl_requests/products/1.json`

or you can add all products stored in products folder using .sh command: <br />
`curl_requests/add_products.sh` <br />

to show detailed information of the product by id use: <br />
`curl -X GET localhost:5000/productsdb -H 'Content-Type: application/json' -d '{"database": "ProductsDB", "collection": "products", "Filter" : {"id" : 1}}'`

or .sh file:
`curl_requests/get_product.sh` <br />

to delete product by id use: <br />
`curl -X DELETE localhost:5000/productsdb -H 'Content-Type: application/json' -d '{"database": "ProductsDB", "collection": "products", "Filter" : {"id" : 1}}'`

or .sh file:
`curl_requests/delete_product.sh` <br />

to filter product by value-key use: <br />
`curl -X GET localhost:5000/productsdb -H 'Content-Type: application/json' -d '{"database": "ProductsDB", "collection": "products", "Filter" : {"description" : "Laptop"}}'`

or .sh file:
`curl_requests/filter_product.sh` <br />

# **Requirements**

Flask-PyMongo==2.3.0 <br />
Flask>=0.11 <br />
click>=7.1.2 <br />
colorama <br />
itsdangerous>=2.0 <br />
Jinja2>=3.0 <br />
MarkupSafe>=2.0 <br />
Werkzeug>=2.0 <br />
PyMongo>=3.3 <br />

