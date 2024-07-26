import pandas as pd
from src.data_preprocessing import load_data, clean_data, save_processed_data
from src.feature_extraction import extract_features, save_features
from src.model_training import train_model, save_model
from src.model_evaluation import evaluate_model
from src.model_deployment import app as deployment_app

def run_data_preprocessing():
    true_path = 'data/raw/True.csv'
    false_path = 'data/raw/Fake.csv'
    processed_path = 'data/processed/combined.csv'
    
    df = load_data(true_path, false_path)
    df = clean_data(df)
    save_processed_data(df, processed_path)
    print("Data preprocessing completed.")

def run_feature_extraction():
    data_path = 'data/processed/combined.csv'
    feature_path = 'data/processed/features.pkl'
    vectorizer_path = 'data/processed/vectorizer.pkl'
    
    df = pd.read_csv(data_path)
    features, vectorizer = extract_features(df['text'])
    save_features(features, vectorizer, feature_path, vectorizer_path)
    print("Feature extraction completed.")

def run_model_training():
    feature_path = 'data/processed/features.pkl'
    label_path = 'data/processed/combined.csv'
    model_path = 'models/trained_model.pkl'
    
    features, labels = pd.read_pickle(feature_path), pd.read_csv(label_path)['label']
    model = train_model(features, labels)
    save_model(model, model_path)
    print("Model training completed.")

def run_model_evaluation():
    model_path = 'models/trained_model.pkl'
    feature_path = 'data/processed/features.pkl'
    label_path = 'data/processed/combined.csv'
    
    model = pd.read_pickle(model_path)
    features, labels = pd.read_pickle(feature_path), pd.read_csv(label_path)['label']
    evaluate_model(model, features, labels)
    print("Model evaluation completed.")

def run_model_deployment():
    deployment_app.run(debug=True)

if __name__ == "__main__":
    run_data_preprocessing()
    run_feature_extraction()
    run_model_training()
    run_model_evaluation()
    # Uncomment the following line to start the Flask server for deployment
    # run_model_deployment()
