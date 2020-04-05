# main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PatientRq(BaseModel):
    name: str
    surename: str

class PatientResp(BaseModel):
    id: int = 1
    patient: Dict

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/patient")
def create_patient(rq: PatientRq):
    return PatientResp(patient=rq.dict())

