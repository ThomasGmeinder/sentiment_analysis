# Deployment Guide

This guide will help you deploy the Sentiment Analysis app with the backend on Render and the frontend on GitHub Pages.

## Architecture

- **Backend (API)**: Flask app with DistilBERT model → Deployed on Render
- **Frontend (UI)**: Static HTML/CSS/JS → Deployed on GitHub Pages

## Step 1: Deploy Backend to Render

1. **Sign up/Login to Render**: Go to https://render.com and create a free account

2. **Create a New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `ThomasGmeinder/sentiment_analysis`
   - Configure the service:
     - **Name**: `sentiment-analysis-api` (or your choice)
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Instance Type**: Free

3. **Deploy**:
   - Click "Create Web Service"
   - Wait for the deployment (first deploy takes 5-10 minutes as it downloads the model)
   - Note your API URL (e.g., `https://sentiment-analysis-api.onrender.com`)

## Step 2: Configure Frontend for GitHub Pages

1. **Update the API URL in the frontend**:
   - Edit `docs/index.html`
   - Find the line: `const API_URL = 'YOUR_RENDER_API_URL_HERE/analyze';`
   - Replace with your Render URL: `const API_URL = 'https://your-app-name.onrender.com/analyze';`

2. **Commit the changes**:
   ```bash
   git add docs/index.html
   git commit -m "Configure API URL for production"
   git push origin main
   ```

## Step 3: Enable GitHub Pages

1. **Go to your GitHub repository settings**:
   - Navigate to `https://github.com/ThomasGmeinder/sentiment_analysis/settings/pages`

2. **Configure GitHub Pages**:
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/docs`
   - Click "Save"

3. **Access your live app**:
   - Your app will be available at: `https://thomasgmeinder.github.io/sentiment_analysis/`
   - It may take 1-2 minutes for GitHub Pages to build

## Testing

1. Open your GitHub Pages URL
2. Enter some text like "I love this!"
3. Click "Analyze Sentiment"
4. You should see the sentiment result with confidence score

## Troubleshooting

### Backend Issues

- **Render deployment fails**: Check the build logs in Render dashboard
- **502 Bad Gateway**: The app is still loading (model download takes time on first start)
- **Memory issues**: Upgrade to a paid Render instance with more RAM

### Frontend Issues

- **API URL not configured error**: Update the API_URL in `docs/index.html`
- **CORS errors**: Make sure flask-cors is installed and enabled in `app.py`
- **Connection refused**: Check that your Render backend is running

### Free Tier Limitations

- **Render Free Tier**: Apps spin down after 15 minutes of inactivity, first request may take 30-60 seconds to wake up
- **Solution**: Use Render's paid tier or consider other hosting options

## Local Development

To run locally:

```bash
# Backend
source .venv/bin/activate
python app.py
# Runs on http://localhost:5001

# Frontend (for local testing)
# Use templates/index.html which connects to local backend
```

## Alternative Deployment Options

If Render doesn't work well, consider:

- **Railway**: https://railway.app (similar to Render)
- **Fly.io**: https://fly.io (more technical but powerful)
- **Heroku**: https://heroku.com (requires credit card)
- **Google Cloud Run**: Free tier available

## Cost

- **GitHub Pages**: Free
- **Render Free Tier**: Free (with limitations)
- **Total Cost**: $0/month for hobby projects

## Notes

- First API call after inactivity will be slow (30-60 seconds) on free tier
- Model is ~250MB and downloads on first deployment
- CORS is enabled to allow GitHub Pages domain to access the API
