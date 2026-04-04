from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Wassim IA est en ligne ! Utilise /chat pour parler."
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key="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"
)

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system",
             "content": "Tu es une IA appelée Wassim, intelligente et utile."},

            {"role": "user",
             "content": user_message}
        ]
    )

    reply = response.choices[0].message.content

    return jsonify({"reply": reply})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)