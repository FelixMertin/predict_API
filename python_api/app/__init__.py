from flask import Flask
from flask_restplus import Api
from .config import Config

app = Flask(__name__)

api = Api(app, prefix='/api')

# Add to api-key to the http header
parser = api.parser()
parser.add_argument('api-key', type=str, location='headers')


from .api_v1 import resources