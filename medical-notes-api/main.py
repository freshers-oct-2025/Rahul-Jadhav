import sys
import os
sys.path.append(os.path.dirname(__file__))

from fastapi import FastAPI
from api.routes.soap_routes import router as soap_router
from api.routes.progress_routes import router as progress_router
from core.database import Base, engine
from models.note import Transcript, SOAPNote, ProgressNote


app = FastAPI(title="Medical Notes API")

app.include_router(soap_router, prefix="/generate")
app.include_router(progress_router, prefix="/generate")

@app.on_event("startup")
def init_db():
    Base.metadata.create_all(bind=engine)
