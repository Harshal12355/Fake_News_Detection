# Model Evaluation Script

# src/model_evaluation.py
import pickle
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd

def load_model(model_path):
    with open(model_path, 'rb') as f:
        return pickle.load(f)

def load_data(feature_path, label_path):
    with open(feature_path, 'rb') as f:
        features = pickle.load(f)
    df = pd.read_csv(label_path)
    return features, df['label']

def evaluate_model(model, features, labels):
    y_pred = model.predict(features)
    print(classification_report(labels, y_pred))
    print(confusion_matrix(labels, y_pred))

if __name__ == "__main__":
    model_path = 'models/trained_model.pkl'
    feature_path = 'data/processed/features.pkl'
    label_path = 'data/processed/combined.csv'
    
    model = load_model(model_path)
    features, labels = load_data(feature_path, label_path)
    evaluate_model(model, features, labels)
