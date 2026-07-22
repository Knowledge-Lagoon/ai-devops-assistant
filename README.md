# AI DevOps Assistant

A minimal FastAPI-based starter project for an AI DevOps assistant.

## Structure

- app/main.py: FastAPI entry point
- app/ai/base.py: abstract AI provider interface
- app/ai/gemini_provider.py: example Gemini provider implementation
- app/config.py: environment loading helper

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your Gemini API key in the .env file.
3. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```
