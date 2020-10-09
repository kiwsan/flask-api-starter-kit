from flask import request
from flask_restplus import Resource, Namespace
# https://github.com/noirbizarre/flask-restplus/blob/4b58cb3e13b7720cb35a39f50d4683770ab72574/examples/todo.py

api = Namespace('value-api', description='value related operations')

# request validators
parser = api.parser()


@api.route('/')
class Values(Resource):
    def get(self):
        '''Get All'''
        return [
            {'hello': 'world'},
            {'hello': 'world'},
            {'hello': 'world'}
        ]

    @api.doc(parser=parser)
    def post(self):
        '''Create'''
        return {'status': 'Created'}, 201


@api.route('/<int:id>')
@api.response(404, 'Object not found')
@api.param('id', 'The task identifier')
class Value(Resource):
    def get(self, id):
        '''Get by Id'''
        return {'hello': "my param is {0}".format(id)}

    @api.doc(responses={204: 'Todo deleted'})
    def delete(self, id):
        '''Delete a given resource'''
        return '', 204

    @api.doc(parser=parser)
    def put(self, todo_id):
        '''Update a given resource'''
        return 'Updated'
