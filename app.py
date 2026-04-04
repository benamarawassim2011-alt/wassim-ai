# app.py
from flask import Flask, request, jsonify
import openai
import os

# --- CONFIGURATION DE L'API OPENAI ---
openai.api_key = os.getenv("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")  # Ton clé OpenAI depuis Render

# --- INITIALISATION DE FLASK ---
app = Flask(__name__)

# --- ROUTE RACINE / ---
@app.route("/", methods=["GET"])
def home():
    return "Wassim IA est en ligne ! Utilise /chat pour parler."

# --- ROUTE /chat POUR L'IA ---
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        prompt = data.get("message", "")
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        answer = response.choices[0].message.content
        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- LANCEMENT DE L'APPLICATION ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render fournit le PORT automatiquement
    app.run(host="0.0.0.0", port=port)