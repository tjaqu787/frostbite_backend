import numpy as np
import tensorflow as tf
from tensorflow import keras

def load_model(model_path='roof_damage_model.h5'):
    model = keras.models.load_model(model_path)
    return model

    