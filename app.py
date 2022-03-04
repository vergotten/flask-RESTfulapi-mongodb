from flask import Flask, request, json, Response, jsonify
from pymongo import MongoClient

app = Flask(__name__)

class MongoREST:
    """
    MongoDB object instance with implementation of CRUD methods.

    """
    def __init__(self, data: json):
        """
        Constructor which takes a json file as a parameter.

        :param data:
        """
        self.client = MongoClient("mongodb://localhost:27017/")
        self.data = data # input data in json format (database -> collection -> document)
        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]

    def create(self, data: json) -> dict:
        """
        Create new record.

        :param data:
        :return:
        """
        try:
            new_document = data['Document']
            response = self.collection.insert_one(new_document)
            output = {'Status': 'Successfully Inserted',
                      'Document_ID': str(response.inserted_id)}
            return output
        except Exception as e:
            return jsonify({'error': str(e)})


    def read(self) -> list:
        """
        Read record.

        :return:
        """
        try:
            if 'Filter' in self.data:
                filt = self.data['Filter']
                documents = self.collection.find(filt)
            else:
                documents = self.collection.find()
            output = [{item: data[item] for item in data if item != '_id'} for data in documents] # to get rid of '_id'
            return output
        except Exception as e:
            return jsonify({'error': str(e)})

    def update(self) -> dict:
        """
        Update record.

        :return:
        """
        try:
            filt = self.data['Filter']
            updated_data = {"$set": self.data['DataToBeUpdated']}
            response = self.collection.update_one(filt, updated_data)
            output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated"}
            return output
        except Exception as e:
            return jsonify({'error': str(e)})

    def delete(self, data: json) -> dict:
        """
        Delete record.

        :param data:
        :return:
        """
        try:
            filt = data['Filter']
            response = self.collection.delete_one(filt)
            output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found"}
            return output
        except Exception as e:
            return jsonify({'error': str(e)})


@app.route('/')
def index():
    return Response(response=json.dumps({"Status": "The request has succeeded"}),
                    status=200,
                    mimetype='application/json')


@app.route('/productsdb', methods=['GET'])
def mongodb_read():
    data = request.json
    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Bad Request"}),
                        status=400,
                        mimetype='application/json')
    obj = MongoREST(data)
    response = obj.read()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


@app.route('/productsdb', methods=['POST'])
def mongodb_create():
    data = request.json
    if data is None or data == {} or 'Document' not in data:
        return Response(response=json.dumps({"Error": "Bad Request"}),
                        status=400,
                        mimetype='application/json')
    data_obj = MongoREST(data)
    response = data_obj.create(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


@app.route('/productsdb', methods=['DELETE'])
def mongodb_delete():
    data = request.json
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Bad Request"}),
                        status=400,
                        mimetype='application/json')
    data_obj = MongoREST(data)
    response = data_obj.delete(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=False, port=5000)

