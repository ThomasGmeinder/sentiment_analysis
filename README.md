# Sentiment Analysis Web App

A fully browser-based web application that analyzes text sentiment using DistilBERT AI model.

🌐 **Live Demo**: [https://thomasgmeinder.github.io/sentiment_analysis/](https://thomasgmeinder.github.io/sentiment_analysis/)

## Features

- 🚀 **Runs entirely in your browser** - No backend required
- 🔒 **Privacy first** - Your data never leaves your device
- ⚡ **Fast after first load** - Model cached locally
- 🎨 **Beautiful UI** - Color-coded results (Green for positive, Red for negative)
- 📊 **Confidence scores** - See how confident the AI is
- 🤖 **DistilBERT powered** - State-of-the-art sentiment analysis

## How It Works

This app uses [Transformers.js](https://huggingface.co/docs/transformers.js) to run a pre-trained DistilBERT model directly in your browser:

- **Model**: distilbert-base-uncased-finetuned-sst-2-english
- **Size**: ~80MB (quantized, downloads once)
- **Performance**: 100-500ms per analysis on modern devices
- **Technology**: JavaScript + WebAssembly + ONNX Runtime

## Usage

1. Visit https://thomasgmeinder.github.io/sentiment_analysis/
2. Wait for model to load (first visit only, ~1 minute)
3. Enter or edit text in the textarea
4. Click "Analyze Sentiment" or press Enter
5. View results with confidence score

## Local Development

Simply open `docs/index.html` in your browser:

```bash
open docs/index.html
# or
python3 -m http.server 8000 --directory docs
# Then visit http://localhost:8000
```

No dependencies, no installation, no build step!

## Deployment

Already deployed on GitHub Pages! To deploy your own:

1. Fork this repository
2. Go to Settings → Pages
3. Source: Deploy from branch `main`
4. Folder: `/docs`
5. Save

Your app will be live at: `https://YOUR_USERNAME.github.io/sentiment_analysis/`

## Architecture

```
┌─────────────────────────────────────┐
│         GitHub Pages                │
│                                     │
│  ┌───────────────────────────────┐ │
│  │     docs/index.html           │ │
│  │  (HTML + CSS + JavaScript)    │ │
│  │                               │ │
│  │  ┌─────────────────────────┐  │ │
│  │  │   Transformers.js CDN   │  │ │
│  │  │   (from jsdelivr)       │  │ │
│  │  └─────────────────────────┘  │ │
│  │              ↓                │ │
│  │  ┌─────────────────────────┐  │ │
│  │  │  DistilBERT Model       │  │ │
│  │  │  (from Hugging Face)    │  │ │
│  │  │  Cached in browser      │  │ │
│  │  └─────────────────────────┘  │ │
│  └───────────────────────────────┘ │
└─────────────────────────────────────┘
```

## Technologies

- **Transformers.js** - Run Hugging Face models in the browser
- **DistilBERT** - Efficient transformer model for sentiment analysis
- **ONNX Runtime** - High-performance inference engine
- **WebAssembly** - Near-native performance in the browser
- **Pure Vanilla JS** - No frameworks, no build tools

## Why Browser-Based?

- ✅ **$0 hosting costs** - No backend servers needed
- ✅ **Privacy** - Data never sent to any server
- ✅ **Offline capable** - Works without internet after first load
- ✅ **Instant deployment** - Just push to GitHub Pages
- ✅ **No maintenance** - No servers to manage or scale

## Performance

| Device | First Load | Subsequent Analyses |
|--------|-----------|---------------------|
| Desktop | 30-60s | 100-300ms |
| Laptop | 60-90s | 200-500ms |
| Modern Phone | 90-120s | 500-1000ms |

Model is cached after first load, so subsequent visits are instant!

## Browser Compatibility

Works on all modern browsers:
- Chrome/Edge 90+
- Firefox 89+
- Safari 15.4+
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

MIT

---

Built with ❤️ using Transformers.js and DistilBERT
