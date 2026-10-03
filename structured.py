import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.5-flash-lite")


def safe_ask(prompt, max_tokens=500):
    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "max_output_tokens": max_tokens,
                "temperature": 0.5,
                "response_mime_type": "application/json",
            }
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"


prompt = """Extract name and age from this text and return as JSON with keys "name" and "age":
"My name is Muni and I am 22 years old." """

result = safe_ask(prompt)
print("Raw:", result)

try:
    data = json.loads(result)
    print("Parsed:", data)
except json.JSONDecodeError:
    print("Could not parse JSON, model didn't follow format")