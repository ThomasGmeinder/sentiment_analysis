from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import torch

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load pre-trained sentiment analysis model
print("Loading sentiment analysis model...")
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)
print("Model loaded successfully!")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        text = data.get('text', '')

        if not text.strip():
            return jsonify({'error': 'Please enter some text to analyze'}), 400

        # Perform sentiment analysis
        result = sentiment_analyzer(text)[0]

        # Convert model output to our format
        label = result['label']
        score = result['score']

        # Map POSITIVE/NEGATIVE to positive/negative/neutral
        if label == 'POSITIVE':
            sentiment = 'positive'
        elif label == 'NEGATIVE':
            sentiment = 'negative'
        else:
            sentiment = 'neutral'

        return jsonify({
            'sentiment': sentiment,
            'confidence': round(score * 100, 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
