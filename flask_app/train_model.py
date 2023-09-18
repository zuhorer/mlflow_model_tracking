from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_and_save_model(run_name):
    print("training and saving the model")
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    model_filename = f"{run_name.replace(' ', '_')}.pkl"
    joblib.dump(model, model_filename)
    return model, X_test, y_test
