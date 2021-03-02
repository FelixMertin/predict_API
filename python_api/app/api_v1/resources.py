from flask import request
from flask_restplus import Resource
import os
from app import api, parser
from app.api_v1.validate import ValidPredAPI
from app.api_v1.security import require_auth
from app.controller.predict import run_predict

#Turn warnings off 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Create an instance of the API validation schema for the predict endpoint
validPred = ValidPredAPI.validPredModel


class SecureResource(Resource):
    """ Adds the require authentication decorator via Class attribute"""
    method_decorators = [require_auth]

@api.route("/predict")
class Predict(SecureResource):
    """
    Specification:
     - Presupposition:  Model need to be given
     - Result: Returning a dictionary with the predictions
     - Effect: None
    """

    @api.doc('NLP Endpoint', parser=parser, body=validPred)
    def post(self):
            # Checks if posted data is the job_uri  or is it actually needed to check for a file type
            prediction_task = request.json.get("prediction_task")
            if request.json.get("text"):
                #if prediction_task == "NER":
                text = request.json["text"]

                predictions = run_predict(prediction_task="NER", model_name='',
                                          tokenized_data="", text=text)
                print(f"This is our prediction: {predictions}")

                response_object = {
                    'status' : 'success',
                    'prediction': predictions
                }

                return response_object, 200

                """
                else:
                    text = request.json["text"]

                    tokenized_data = run_tokenization(text)
                    print(f"The tokenized data: {tokenized_data}")
                    print('Tokenization done.')

                    predictions = run_predict(prediction_task="Spacy",
                                              model_name='./python_api/app/pretrained/pretrained_model.h5',
                                              tokenized_data=tokenized_data, text=text)
                    print(f"This is our prediction: {predictions}")

                    response_object = {
                        'status': 'success',
                        'prediction': predictions
                    }

                    return response_object, 200
                """