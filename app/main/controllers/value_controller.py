from flask import request
from flask_restplus import Resource, Namespace

api = Namespace('value', description='value related operations')


@api.route('/')
class Get(Resource):
    def get(self):
        return {'hello': 'world'}
