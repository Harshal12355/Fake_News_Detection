# Model Deployment Script

from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

def load_model(model_path):
    with open(model_path, 'rb') as f:
        return pickle.load(f)

def load_vectorizer(vectorizer_path):
    with open(vectorizer_path, 'rb') as f:
        return pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data['text']
    vectorizer = load_vectorizer('data/processed/vectorizer.pkl')
    features = vectorizer.transform([text])
    model = load_model('models/trained_model.pkl')
    prediction = model.predict(features)[0]
    return jsonify({'prediction': 'True' if prediction == 1 else 'False'})

if __name__ == "__main__":
    app.run(debug=True)
