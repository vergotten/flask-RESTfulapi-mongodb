curl -X DELETE localhost:5000/productsdb -H 'Content-Type: application/json' -d '{"database": "ProductsDB", "collection": "products", "Filter" : {"id" : 1}}'