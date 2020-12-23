# Importing Libraries
import numpy as np
import tensorflow as tf

from tensorflow.keras.models import model_from_json
from tensorflow.python.keras.backend import set_session

# Initializing TF Session
config = tf.compat.v1.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.15
session = tf.compat.v1.Session(config=config)
set_session(session)


class FacialExpressionModel(object):
    # List of Emotions
    EMOTIONS_LIST = ["Angry", "Disgust",
                     "Fear", "Happy",
                     "Neutral", "Sad",
                     "Surprise"]

    def __init__(self, model_json, model_h5):
        # load model from JSON file
        with open(model_json, 'r') as json_file:
            loaded_model_json = json_file.read()
        self.loaded_model = model_from_json(loaded_model_json)

        # load weights into the new model
        self.loaded_model.load_weights(model_h5)

    # Function to predict emotion
    def predict_emotion(self, img):
        global session
        set_session(session)
        self.preds = self.loaded_model.predict(img)
        return FacialExpressionModel.EMOTIONS_LIST[np.argmax(self.preds)]
