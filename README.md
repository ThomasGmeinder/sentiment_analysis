# Sentiment Analysis Web App

A fully browser-based web application that analyzes text sentiment using DistilBERT AI model.

🌐 **Live Demo**: [https://thomasgmeinder.github.io/sentiment_analysis/](https://thomasgmeinder.github.io/sentiment_analysis/)

## Features

- 🚀 **Runs entirely in your browser** - No backend required
- ⚡ **GPU accelerated** - Auto-detects AMD, Intel, Apple, NVIDIA GPUs via WebGPU
- 🔒 **Privacy first** - Your data never leaves your device
- 💨 **Fast after first load** - Model cached locally
- 🎨 **Beautiful UI** - Color-coded results (Green for positive, Red for negative)
- 📊 **Real-time metrics** - Shows confidence score, device used, and inference time
- 🤖 **DistilBERT powered** - State-of-the-art sentiment analysis

## How It Works

This app uses [Transformers.js](https://huggingface.co/docs/transformers.js) to run a pre-trained DistilBERT model directly in your browser:

- **Model**: distilbert-base-uncased-finetuned-sst-2-english
- **Size**: ~80MB (quantized, downloads once)
- **Performance**: 100-500ms per analysis on modern devices
- **Technology**: JavaScript + WebAssembly + ONNX Runtime

## GPU Acceleration

The app automatically detects and uses GPU acceleration via **WebGPU** when available:

### Supported Hardware

| Platform | GPU Detected | AI Accelerator | Status |
|----------|-------------|----------------|--------|
| 🎮 **AMD Ryzen AI** | Radeon 3.5 iGPU (Strix/Halo) | - | ✅ GPU via WebGPU |
| 💎 **Intel** | Iris Plus, Arc (Gen-11+) | - | ✅ GPU via WebGPU |
| 🍎 **Apple** | M1/M2/M3/M4 GPU | Neural Engine | ✅ GPU via WebGPU<br>⚠️ Neural Engine not accessible |
| 🟢 **NVIDIA** | GeForce, RTX | - | ✅ GPU via WebGPU |
| 📱 **iPhone/iPad** | A-series GPU | Neural Engine | ✅ GPU via Metal<br>⚠️ Neural Engine not accessible |
| 🤖 **Android** | Adreno, Mali | NPU/TPU | ✅ GPU via Vulkan<br>⚠️ NPU not accessible |

### Performance Comparison

| Device | CPU (Fallback) | GPU (WebGPU) | Speedup |
|--------|---------------|--------------|---------|
| Desktop (discrete GPU) | 200-300ms | 30-80ms | **5-10x faster** |
| Laptop (iGPU) | 300-500ms | 100-200ms | **2-3x faster** |
| Modern Phone | 500-1000ms | 200-400ms | **2-3x faster** |

### Browser Requirements for GPU

- **Chrome/Edge 113+**: WebGPU enabled by default
- **Safari 18+** (macOS Sonoma+, iOS 18+): Full WebGPU support
- **Firefox 126+**: WebGPU available (experimental)

**Note**: The app gracefully falls back to CPU (WebAssembly) on older browsers or devices without WebGPU support. CPU performance is still fast enough for real-time analysis!

### Checking GPU Usage

Open browser console (F12) to see GPU detection:
```
✅ WebGPU available!
🎮 AMD GPU detected! Perfect for Ryzen AI systems.
✅ Loaded with WebGPU acceleration!
Inference: 45ms on WEBGPU
```

Results display show: `Confidence: 99.87% • ⚡ GPU • 45ms`

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
- **WebGPU** - GPU acceleration for AMD, Intel, Apple, NVIDIA
- **WebAssembly** - Near-native CPU performance fallback
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
