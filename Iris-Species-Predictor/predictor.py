# Iris Species Predictor using scikit-learn

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib  # Added for model saving

def load_and_prepare_data():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    # Save the model
    joblib.dump(model, 'iris_model.pkl')
    print("Model saved as iris_model.pkl")
    return model

def evaluate_model(model, X_test, y_test, target_names):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    return predictions

def predict_species(model, features, target_names):
    prediction = model.predict([features])[0]
    return target_names[prediction]

def main():
    df, target_names = load_and_prepare_data()
    X = df.drop('species', axis=1)
    y = df['species']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test, target_names)
    sample_features = X_test.iloc[0].values
    predicted_species = predict_species(model, sample_features, target_names)
    print(f"\nSample Prediction:")
    print(f"Features: {sample_features}")
    print(f"Predicted Species: {predicted_species}")

if __name__ == "__main__":
    main()