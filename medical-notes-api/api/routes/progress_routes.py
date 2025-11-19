# api/routes/progress_routes.py
from fastapi import APIRouter, Depends
from schemas.requests import TranscriptInput
from schemas.responses import ProgressResponse
from services.progress_service import generate_progress
from sqlalchemy.orm import Session
from core.database import get_db

router = APIRouter(tags=["Progress Notes"])

@router.post("/progress", response_model=ProgressResponse)
def create_progress_notes(data: TranscriptInput, db: Session = Depends(get_db)):
    return generate_progress(data.transcript, db)
