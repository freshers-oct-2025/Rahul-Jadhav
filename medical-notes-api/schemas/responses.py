from pydantic import BaseModel

class SOAPResponse(BaseModel):
    subjective: str
    objective: str
    assessment: str
    plan: str

class ProgressResponse(BaseModel):
    patient_status: str
    findings: str
    changes_since_last_visit: str
    medication_compliance: str
    assessment: str
    plan: str
