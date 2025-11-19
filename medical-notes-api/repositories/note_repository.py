# repositories/note_repository.py
from sqlalchemy.orm import Session
from models.note import SOAPNote, ProgressNote, Transcript

def save_transcript(db: Session, transcript_text: str, patient_id: int | None = None):
    t = Transcript(transcript_text=transcript_text, patient_id=patient_id)
    db.add(t)
    db.commit()
    db.refresh(t)
    return t

def save_soap_note(db: Session, transcript_id: int, soap_json: dict):
    note = SOAPNote(
        transcript_id=transcript_id,
        subjective=soap_json.get("subjective"),
        objective=soap_json.get("objective"),
        assessment=soap_json.get("assessment"),
        plan=soap_json.get("plan"),
    )
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

def save_progress_note(db: Session, transcript_id: int, progress_json: dict):
    note = ProgressNote(
        transcript_id=transcript_id,
        patient_status=progress_json.get("patient_status"),
        findings=progress_json.get("findings"),
        changes_since_last_visit=progress_json.get("changes_since_last_visit"),
        medication_compliance=progress_json.get("medication_compliance"),
        assessment=progress_json.get("assessment"),
        plan=progress_json.get("plan"),
    )
    db.add(note)
    db.commit()
    db.refresh(note)
    return note
