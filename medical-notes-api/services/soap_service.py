# services/soap_service.py
import json
from core.llm_client import call_ollama
from repositories.note_repository import save_transcript, save_soap_note
from sqlalchemy.orm import Session

def generate_soap(transcript: str, db: Session):
    
    t = save_transcript(db, transcript_text=transcript)

    prompt = f"""
You are a medical documentation AI.

Convert the following patient consultation transcript into a structured SOAP note.

Return JSON in this format:

{{
    "subjective": "",
    "objective": "",
    "assessment": "",
    "plan": ""
}}

Transcript:
{transcript}
"""
    result = call_ollama(prompt)
    soap_json = json.loads(result)

    
    save_soap_note(db, transcript_id=t.id, soap_json=soap_json)

    return soap_json
