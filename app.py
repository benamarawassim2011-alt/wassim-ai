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

if __name__ == "__main__":
    app.run(debug=True)