import os
import numpy as np
import joblib

class Predict(object):
    def __init__(self):
        """Initializes the serving state, reads a trained model"""
        # Ensure the model path is correct, use an environment variable or direct path
        model_path = os.path.join(os.environ.get("ARTIFACT_FILES_PATH", "/mnt/models"), "xgboost.pkl")
        self.model = joblib.load(model_path)
        print("Initialization Complete")

    def predict(self, inputs):
        """Serves a prediction request using a trained model"""
        # Ensure inputs are correctly shaped
        input_vector = np.array(inputs)
        input_data = input_vector.reshape(1, -1)
        return self.model.predict(input_data).tolist()
