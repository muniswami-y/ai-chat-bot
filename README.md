# AI Chat Application

Module 3 project: LLM APIs & Application Development (Day 11-15).

## Setup
1. Copy `.env.example` to `.env` and add your Gemini API key.
2. `pip install -r requirements.txt`
3. Run `python app.py` and open http://127.0.0.1:5000

## Day 11: Connecting to an LLM API
Set up a Gemini API key, stored securely in a .env file (never committed to GitHub, protected by .gitignore). Installed google-generativeai and python-dotenv. Wrote test.py to confirm the connection.

## Day 12: Chat History and Messages
Built chat.py using start_chat() to keep conversation history automatically. Added a system_instruction to set the AI's role/behavior. Used generation_config to control temperature and max_output_tokens.

## Day 13: Structured Responses, Error Handling, Cost Management
Wrote safe_ask() which wraps API calls in try/except. Asked the model to return strict JSON and parsed it with json.loads(). Managed cost by setting max_output_tokens on every call.

## Day 14: AI Chat Application
Built a Flask backend (app.py) with a /chat API endpoint connected to the Gemini API, and a basic HTML/JS frontend (templates/index.html).

## Day 15: Deployment
Deployed live on Render, connected to GitHub for auto-deploy. API key stored as an environment variable on Render, not in code.
