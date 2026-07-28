# AI DevOps Assistant

A minimal FastAPI-based starter project for an AI DevOps assistant.

## Structure

- `app/main.py`: FastAPI entry point
- `app/ai/base.py`: Abstract AI provider interface
- `app/ai/gemini_provider.py`: Example Gemini provider implementation
- `app/config.py`: Environment loading helper
- `app/rag/document_loader.py`: Utility for loading and processing documents from a folder (supports `.txt`, `.md`, `.pdf`, and `.docx` files).

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your Gemini API key in the `.env` file.
3. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```

## Features

- **Document Loading**: The `document_loader.py` file provides functionality to load documents from a folder and process them based on their file type.
- **AI Integration**: Easily extendable to integrate with AI providers like Gemini.