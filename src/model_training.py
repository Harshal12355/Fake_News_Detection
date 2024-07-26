# Model Training Script

import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def load_data(feature_path, label_path):
    with open(feature_path, 'rb') as f:
        features = pickle.load(f)
    df = pd.read_csv(label_path)
    return features, df['label']

def train_model(features, labels):
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    return model

def save_model(model, model_path):
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    feature_path = 'data/processed/features.pkl'
    label_path = 'data/processed/combined.csv'
    model_path = 'models/trained_model.pkl'
    
    features, labels = load_data(feature_path, label_path)
    model = train_model(features, labels)
    save_model(model, model_path)
