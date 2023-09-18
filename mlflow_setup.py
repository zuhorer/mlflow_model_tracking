import mlflow
import mlflow.sklearn
from train_model import train_and_save_model


counter = 0  # Initialize a counter
model_name = "demo"

def mlflow_run():
    global counter  # Declare counter as global to modify it
    global model_name
    if model_name is None:
        model_name = input("Enter the name of the model for this experiment: ")
    run_name = f"{model_name}{counter / 10:.1f}"  # Create  new run name

    with mlflow.start_run(run_name=run_name) as run:
        model, X_test, y_test = train_and_save_model(run_name)
        mlflow.log_param("n_estimators", model.n_estimators)
        mlflow.log_metric("accuracy", model.score(X_test, y_test))

        # Log the model to MLflow
        mlflow.sklearn.log_model(model, run_name)

    counter += 1  # Increment the counter
