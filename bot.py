from flask import Flask, request
import requests
import os

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAcZCsxsjsInUBRzZAssJLYwZBgo7EB2YCGnJ7YwI7gKB1eJ6bej49giNZ"  # Token mu kui
VERIFY_TOKEN = "antique_bot_2026"  # Sing tak kei nduwur kui

@app.route('/webhook', methods=['GET'])
def verify():
    if request.args.get('hub.verify_token') == VERIFY_TOKEN:
        return request.args.get('hub.challenge')
    return "Verification failed", 403

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if data['object'] == 'page':
        for entry in data['entry']:
            for event in entry['messaging']:
                if 'message' in event and 'text' in event['message']:
                    sender_id = event['sender']['id']
                    message_text = event['message']['text'].lower()
                    
                    # Balasan otomatis wkwk
                    if 'harga' in message_text:
                        reply = "Siap mas/mbak 🙏 Untuk harga antique silakan chat admin ya. Mau liat katalog?"
                    else:
                        reply = "Halo! Selamat datang di AntiqueboT 🔥 Ada yang bisa dibantu?"
                    
                    send_message(sender_id, reply)
    return "ok", 200

def send_message(recipient_id, message_text):
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    payload = {"recipient": {"id": recipient_id}, "message": {"text": message_text}}
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(port=5000)