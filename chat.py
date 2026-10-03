import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    "gemini-3.8-flash",
    system_instruction="You are a helpful, friendly assistant. Keep answers short."
)

chat = model.start_chat(history=[])

generation_config = {
    "temperature": 0.7,
    "max_output_tokens": 200,
}

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = chat.send_message(user_input, generation_config=generation_config)
    print("AI:", response.text)
