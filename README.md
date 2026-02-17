# Sentiment Analysis Web App

A simple web application that analyzes text sentiment using a pre-trained DistilBERT model.

## Features

- Real-time sentiment analysis (Positive/Negative)
- Beautiful, intuitive web interface
- Color-coded results (Green for positive, Red for negative)
- Confidence scores for each prediction
- No training required - uses pre-trained model

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and go to:
```
http://localhost:5000
```

3. Enter any text in the textarea and click "Analyze Sentiment" to see the results!

## How It Works

- **Backend**: Flask server that loads a pre-trained DistilBERT model from Hugging Face
- **Model**: distilbert-base-uncased-finetuned-sst-2-english
- **Frontend**: Simple HTML/CSS/JavaScript interface

## Usage

1. Type or paste text into the text area
2. Click "Analyze Sentiment" or press Enter
3. View the sentiment result with confidence score

Enjoy analyzing sentiment!
