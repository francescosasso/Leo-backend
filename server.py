from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def home():
    return "Leó backend attivo"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json

    try:
        r = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4o-mini",
                "messages": data.get("messages", []),
                "temperature": data.get("temperature", 0.7),
                "max_tokens": data.get("max_tokens", 400)
            },
            timeout=60
        )

        return jsonify(r.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # 🔴 QUESTO È IL FIX CRITICO PER RENDER
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
