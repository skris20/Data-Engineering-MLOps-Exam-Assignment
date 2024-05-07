import os
import numpy as np
import hsfs
import joblib

class Predict(object):

    def __init__(self):
        """ Initializes the serving state, reads a trained model"""
        # load the trained model
        self.model = joblib.load(os.environ["ARTIFACT_FILES_PATH"] + "/xgboost.pkl")
        print("Initialization Complete")

    def predict(self, inputs):
        """ Serves a prediction request using a trained model"""
        # Convert inputs to numpy array to handle batch predictions
        inputs_array = np.array(inputs)
        # Check if the input is a single instance or batch
        if inputs_array.ndim == 1:
            # Reshape if a single instance to match input shape expected by the model
            inputs_array = inputs_array.reshape(1, -1)
        # Make predictions
        return self.model.predict(inputs_array).tolist()  # Return predictions as list
