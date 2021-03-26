import numpy as np

from tensorflow.keras.models import model_from_json


class Model(object):
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

        emotion = self.loaded_model.predict(img)
        return Model.EMOTIONS_LIST[np.argmax(emotion)], emotion[0]
