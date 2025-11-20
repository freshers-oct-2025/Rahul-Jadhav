
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from core.database import Base

class Transcript(Base):
    __tablename__ = "transcripts"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, index=True, nullable=True)
    transcript_text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class SOAPNote(Base):
    __tablename__ = "soap_notes"

    id = Column(Integer, primary_key=True)
    transcript_id = Column(Integer, ForeignKey("transcripts.id"))
    subjective = Column(Text)
    objective = Column(Text)
    assessment = Column(Text)
    plan = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class ProgressNote(Base):
    __tablename__ = "progress_notes"

    id = Column(Integer, primary_key=True)
    transcript_id = Column(Integer, ForeignKey("transcripts.id"))
    patient_status = Column(Text)
    findings = Column(Text)
    changes_since_last_visit = Column(Text)
    medication_compliance = Column(Text)
    assessment = Column(Text)
    plan = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
