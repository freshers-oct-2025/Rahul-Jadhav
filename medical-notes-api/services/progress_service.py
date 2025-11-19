# services/progress_service.py
import json
from core.llm_client import call_ollama
from repositories.note_repository import save_transcript, save_progress_note
from sqlalchemy.orm import Session

def generate_progress(transcript: str, db: Session):
    
    t = save_transcript(db, transcript_text=transcript)

    prompt = f"""
You are a medical scribe.

Convert the following transcript into a structured progress note.

Return JSON in the following format:

{{
    "patient_status": "",
    "findings": "",
    "changes_since_last_visit": "",
    "medication_compliance": "",
    "assessment": "",
    "plan": ""
}}

Transcript:
{transcript}
"""
    result = call_ollama(prompt)
    progress_json = json.loads(result)

    
    save_progress_note(db, transcript_id=t.id, progress_json=progress_json)

    return progress_json
