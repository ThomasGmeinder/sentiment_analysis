# Sentiment Analysis Web App

A web application that analyzes text sentiment using a pre-trained DistilBERT model.

🌐 **Live Demo**: [https://thomasgmeinder.github.io/sentiment_analysis/](https://thomasgmeinder.github.io/sentiment_analysis/)

## Features

- Real-time sentiment analysis (Positive/Negative)
- Beautiful, intuitive web interface
- Color-coded results (Green for positive, Red for negative)
- Confidence scores for each prediction
- No training required - uses pre-trained model

## Architecture

- **Backend API**: Flask + DistilBERT (deployed on Render)
- **Frontend UI**: Static HTML/CSS/JS (deployed on GitHub Pages)
- **Model**: distilbert-base-uncased-finetuned-sst-2-english

## Deployment

See [DEPLOY.md](DEPLOY.md) for detailed deployment instructions.

### Quick Deploy

1. **Backend**: Deploy to Render
2. **Frontend**: Enable GitHub Pages from `/docs` folder
3. **Configure**: Update API URL in `docs/index.html`

## Local Development

1. Create and activate virtual environment:
```bash
python3.10 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the Flask server:
```bash
python app.py
```

4. Open your browser and go to:
```
http://localhost:5001
```

5. Enter any text in the textarea and click "Analyze Sentiment" to see the results!

## How It Works

- **Backend**: Flask server with CORS support, loads pre-trained DistilBERT model from Hugging Face
- **Model**: distilbert-base-uncased-finetuned-sst-2-english
- **Frontend**: Static web interface that calls the backend API

## Usage

1. Type or paste text into the text area
2. Click "Analyze Sentiment" or press Enter
3. View the sentiment result with confidence score

## Technologies

- Python 3.10+
- Flask 3.0
- Transformers (Hugging Face)
- PyTorch
- DistilBERT model

## License

MIT

---

Enjoy analyzing sentiment!
