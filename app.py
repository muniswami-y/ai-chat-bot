import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

model = genai.GenerativeModel(
    "gemini-3.8-flash",
    system_instruction="You are a helpful, friendly assistant. Keep answers concise."
)
chat = model.start_chat(history=[])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat_api():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    try:
        response = chat.send_message(
            user_message,
            generation_config={"temperature": 0.7, "max_output_tokens": 200}
        )
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
