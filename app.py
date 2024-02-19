# Author: Nolan McKenna 
# Purpose: Create a RESTful microservice that utilizes SwaggerUI
from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, title='RESTful Microservice', description='Implements GET, POST, PUT, and DELETE')

ns = api.namespace('Operations')

data_model = api.model('Data', {
    'key': fields.String(required=True),
    'value': fields.String(required=True)
})

# Data where CRUD operations will be done 
data = {}

@ns.route('/data')
class MyResource(Resource):
    def get(self):
        """Get all data"""
        return data

    @ns.expect(data_model)
    def post(self):
        """Add new data"""
        key = api.payload['key']
        value = api.payload['value']
        data[key] = value
        return {'message': 'Data added successfully'}, 200

    @ns.expect(data_model)
    def put(self):
        """Update existing data"""
        key = api.payload['key']
        value = api.payload['value']
        if key in data: 
            data[key] = value
            return {'message': 'Data updated successfully'}, 200
        else: 
            return {'message': 'Key not found'}, 404

    @ns.expect(data_model)
    def delete(self):
        """Delete existing data"""
        key = api.payload['key']
        if key in data:
            del data[key]
            return {'message': 'Data deleted successfully'}, 200
        else:
            return {'message': 'Key not found'}, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, debug=True)
