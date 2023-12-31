from flask import Flask, request, jsonify
import joblib
from train_model import train_and_save_model  # Import the training function
from mlflow_setup import mlflow_run  # Import the MLflow setup function
# from dotenv import load_dotenv
import os

# Load environment variables from .env file
# load_dotenv()


app = Flask(__name__)

def serve_model():
    @app.route('/predict', methods=['POST'])
    def predict():
        data = request.json
        model_name = data.get('model_name', 'model')  # You can specify the model name in the request
        model_filename = f"{model_name}.pkl"  # Construct the model filename
        model = joblib.load(model_filename)
        prediction = model.predict([data['features']])
        return jsonify({'prediction': int(prediction[0])})

    @app.route('/train', methods=['POST'])
    def train():
        mlflow_run()  # Trigger the MLflow setup
        return jsonify({'message': 'Model trained and logged to MLflow'})
    
    app.run(host='0.0.0.0', port=3000)

