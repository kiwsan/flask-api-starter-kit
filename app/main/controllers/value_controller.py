from flask import request
from flask_restplus import Resource, Namespace

api = Namespace('value-api', description='value related operations')


@api.route('/')
class Get(Resource):
    def get(self):
        return [
            {'hello': 'world'},
            {'hello': 'world'},
            {'hello': 'world'}
        ]

@api.route('/<int:id>')
@api.response(404, 'Todo not found')
@api.param('id', 'The task identifier')
class GetById(Resource):
    def get(self, id):
        return {'hello': "my param is {0}".format(id) }
