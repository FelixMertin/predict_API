from flask_restplus import fields
from app import api

class ValidPredAPI:
    validPredModel = api.model('predicting', {
        'text': fields.String(required=True, description='The text that should be classified'),
        'prediction_task': fields.String(required=True, description='Choose between NER or Text Classification'),
    })