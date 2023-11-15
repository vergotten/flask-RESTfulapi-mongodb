# Flask RESTful API with MongoDB for E-Shop

This repository contains a microservice for an e-shop, implemented using Flask and MongoDB. The microservice is designed to manage products in the warehouse of an e-shop. Each product, such as a phone, has a name, manufacturer, and other parameters.

## Model/Entities

The main entity in this microservice is the `Product`, which represents the goods in the warehouse. Each product has the following fields:

- `identifier (ID)`
- `title`
- `description`
- `parameters`: an array of key/value pairs

## Libraries

This project uses the following libraries:

- `flask`: A lightweight WSGI web application framework.
- `pymongo`: A Python driver for MongoDB.

## Database

Entities are stored in a MongoDB database running at `localhost:27017`.

## Installation

To install the dependencies and libraries, use the following command:
```
pip install -r requirements.txt
```


To launch mongodb in docker use: <br />
```
docker run -d -p 27017:27017 mongo
```

REST API methods: <br />
- Create a new product <br />
- Get a list of product names, with the ability to filter by: <br />

- a) name <br />
- b) the selected parameter and its value <br />
- Get product details by ID <br />

Methods accept JSON as input and return JSON as output. <br />

To launch application use: <br /> 
```
python app.py
```

## Curl commands:

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
```
curl -X POST localhost:5000/productsdb -H 'Content-Type: application/json' -d @curl_requests/products/1.json
```

or you can add all products stored in products folder using .sh command: <br />
```
curl_requests/add_products.sh
```

to show detailed information of the product by id use: <br />
```
curl -X GET localhost:5000/productsdb -H 'Content-Type: application/json' -d '{"database": "ProductsDB", "collection": "products", "Filter" : {"id" : 1}}'
```

or .sh file:
```
curl_requests/get_product.sh
```

to delete product by id use: <br />
```
curl -X DELETE localhost:5000/productsdb -H 'Content-Type: application/json' -d '{"database": "ProductsDB", "collection": "products", "Filter" : {"id" : 1}}'
```

or .sh file:
```
curl_requests/delete_product.sh
```

to filter product by value-key use: <br />
```
curl -X GET localhost:5000/productsdb -H 'Content-Type: application/json' -d '{"database": "ProductsDB", "collection": "products", "Filter" : {"description" : "Laptop"}}'
```

or .sh file:
```
curl_requests/filter_product.sh
```

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

