from flask_restplus import Api
from flask import Blueprint

from app.main.controllers.value_controller import api as value_controller_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK-RESTPlus API',
          version='1.0',
          description='a boilerplate for flask restplus web service')

api.add_namespace(value_controller_ns, path='/api/v1/values')
