from tensorflow.keras.models import load_model
from tensorflow.keras.utils import CustomObjectScope
import numpy as np

def run_tf_predict(model_name, tokenized_data):

        """
         Specification:
         - Presupposition: Tensorflow Model and a tokenized text must be given.
         - Result: Returns the predictions as list
         - Effect: None
        """

        # Spreading the dependent Variables to represent one Observation
        # Before -> shape (94, 34)
        # After Transform -> shape (1, 94, 34)
        matrix_data = np.ndarray(shape=(1, 94, 34))
        matrix_data[0] = tokenized_data
        model = load_model(model_name)
        print(matrix_data.shape)
        prediction = model.predict(matrix_data, verbose=0)

        return prediction[0].tolist()