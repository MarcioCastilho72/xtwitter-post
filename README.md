# 🐦 XTwitter Post Microservice

This microservice posts text and optional images to X (formerly Twitter) using the v1.1 API.

## 🔧 Setup

1. Clone this repo and deploy to [Render](https://render.com/).
2. Use Python 3 environment.

### Required environment variables:

- `CONSUMER_KEY`
- `CONSUMER_SECRET`
- `ACCESS_TOKEN`
- `ACCESS_TOKEN_SECRET`

## 📦 Requirements

- tweepy
- flask
- requests

Install with:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

POST to `/post` with the following JSON body:

```json
{
  "text": "Hello world from Render!",
  "image_url": "https://replicate.delivery/pbxt/your-image.jpg"
}
```

## 📡 Integration

Call this endpoint from n8n or any other tool via HTTP POST.

## 🛠 Hosting

This is configured for Render via `render.yaml`, using port 5000.