# api/routes/soap_routes.py
from fastapi import APIRouter, Depends
from schemas.requests import TranscriptInput
from schemas.responses import SOAPResponse
from services.soap_service import generate_soap
from sqlalchemy.orm import Session
from core.database import get_db

router = APIRouter(tags=["SOAP Notes"])

@router.post("/soap", response_model=SOAPResponse)
def create_soap_notes(data: TranscriptInput, db: Session = Depends(get_db)):
    return generate_soap(data.transcript, db)
