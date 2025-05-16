from flask import Flask, request, jsonify
import tweepy
import requests
from io import BytesIO
import os

app = Flask(__name__)

# Verifica se todas as variáveis de ambiente estão definidas
required_env_vars = ['CONSUMER_KEY', 'CONSUMER_SECRET', 'ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET']
missing_vars = [var for var in required_env_vars if not os.environ.get(var)]
if missing_vars:
    raise EnvironmentError(f"Missing environment variables: {', '.join(missing_vars)}")

# Carrega as credenciais do Twitter
consumer_key = os.environ.get('ybFjGcgFbWDkoe7wfBNB19vNj')
consumer_secret = os.environ.get('rs4iKNXTJmRJMeIZ9hXktBiuUYjcJAZusjZ1D7yhE8ax8qgvio')
access_token = os.environ.get('1923286783917424641-ow59pxKlkeRknVkFw83RiMaDAAaCoz')
access_token_secret = os.environ.get('kfCcokwqOeKIOPWwvF44K8Juofn9PnzZtk9FLVSAHndTZ')

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

@app.route('/post', methods=['POST'])
def post_to_x():
    data = request.json
    text = data.get('text', '')
    image_url = data.get('image_url')

    media_id = None
    if image_url:
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            image = BytesIO(response.content)
            media = api.media_upload(filename='image.jpg', file=image)
            media_id = media.media_id
        except Exception as e:
            return jsonify({"error": "Image upload failed", "details": str(e)}), 500

    try:
        if media_id:
            api.update_status(status=text, media_ids=[media_id])
        else:
            api.update_status(status=text)
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"error": "Tweet failed", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)))