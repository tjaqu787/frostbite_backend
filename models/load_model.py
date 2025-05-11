import numpy as np
import tensorflow as tf
from tensorflow import keras

def load_and_predict( input_data,model_path='roof_damage_model.h5'):
    """
    Load a .h5 model and make inference on input data
    
    Args:
        model_path (str): Path to the .h5 model file
        input_data (numpy.ndarray): Input data for inference
    
    Returns:
        numpy.ndarray: Model predictions
    """
    # Load the model
    model = keras.models.load_model(model_path)
    
    # Print model summary for verification
    print("Model loaded successfully!")
    print("\nModel Summary:")
    model.summary()
    
    # Make inference
    predictions = model.predict(input_data)
    
    return predictions

# Example usage
if __name__ == "__main__":
    # Replace with your model path
    model_path = "your_model.h5"
    