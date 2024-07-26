# Feature Extraction Script

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import pickle

def extract_features(texts):
    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
    features = vectorizer.fit_transform(texts)
    return features, vectorizer

def save_features(features, vectorizer, feature_path, vectorizer_path):
    with open(feature_path, 'wb') as f:
        pickle.dump(features, f)
    with open(vectorizer_path, 'wb') as f:
        pickle.dump(vectorizer, f)

if __name__ == "__main__":
    data_path = 'data/processed/combined.csv'
    feature_path = 'data/processed/features.pkl'
    vectorizer_path = 'data/processed/vectorizer.pkl'
    
    df = pd.read_csv(data_path)
    features, vectorizer = extract_features(df['text'])
    save_features(features, vectorizer, feature_path, vectorizer_path)
