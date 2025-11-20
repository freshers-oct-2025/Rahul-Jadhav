import requests
from fastapi import HTTPException
from core.config import MODEL_NAME, OLLAMA_URL

def call_ollama(prompt: str):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        raise HTTPException(
            status_code=500,
            detail=f"Ollama Error: {response.text}"
        )

    data = response.json()

    if "response" not in data:
        raise HTTPException(
            status_code=500,
            detail="No response returned from LLM."
        )

    return data["response"]
