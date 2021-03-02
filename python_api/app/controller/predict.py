from .predicting.spacy_predict import run_spacy_predict

def run_predict(prediction_task, model_name, tokenized_data, text):
        """
         Specification:
         - Presupposition: Tensorflow Model and a tokenized text must be given.
         - Result: Returns the predictions as list
         - Effect: None
        """

        #if prediction_task == "Text Classification":
        #                prediction = run_tf_predict(model_name, tokenized_data)
        #elif prediction_task == "NER":

        prediction = run_spacy_predict(model_name, text)


        return prediction