# Author: Nolan McKenna 
# Purpose: Create a RESTful microservice that utilizes SwaggerUI
from flask import Flask, request
from flask_restx import Api, Resource, fields, reqparse
import os

app = Flask(__name__)
api = Api(app, title='RESTful Microservice', description='Implements GET, POST, PUT, and DELETE. Also supports /config and /fib paths')

ns = api.namespace('')

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
        
@ns.route('/config')
class ConfigResource(Resource):
    def get(self):
        """Get environment variables"""
        env_vars = {}
        for key, value in os.environ.items():
            env_vars[key] = value
        
        # Write environment variables to log
        print(env_vars)
        
        return env_vars

@ns.route('/fib')
class FibonacciResource(Resource):
    def get(self):
        """Get Fibonacci sequence"""
        length = request.args.get('length', type=int, default=10)  # Get the length from query parameter, default to 10

        if length < 0:
            return {'message': 'Length must be a non-negative integer'}, 400

        fib_sequence = [0, 1]
        for i in range(2, length):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        return fib_sequence


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, debug=True)
