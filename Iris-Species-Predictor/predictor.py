# Iris Species Predictor using scikit-learn

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def load_and_prepare_data():
    """Load the Iris dataset and prepare it for training."""
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

def train_model(X_train, y_train):
    """Train a Random Forest model."""
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test, target_names):
    """Evaluate the model and print accuracy."""
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    return predictions

def predict_species(model, features, target_names):
    """Predict the species for a new sample."""
    prediction = model.predict([features])[0]
    return target_names[prediction]

def main():
    # Load and prepare data
    df, target_names = load_and_prepare_data()
    X = df.drop('species', axis=1)
    y = df['species']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(model, X_test, y_test, target_names)

    # Predict a new sample (example: using the first test sample's features)
    sample_features = X_test.iloc[0].values
    predicted_species = predict_species(model, sample_features, target_names)
    print(f"\nSample Prediction:")
    print(f"Features: {sample_features}")
    print(f"Predicted Species: {predicted_species}")

if __name__ == "__main__":
    main()