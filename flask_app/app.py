
from mlflow_setup import mlflow_run
from serve_model import serve_model
import subprocess

# To train and save the model and start ml flow run

mlflow_run()
# Step 2: Start the MLflow UI
subprocess.Popen(["mlflow", "ui"])
# To serve the model using Flask
serve_model()


