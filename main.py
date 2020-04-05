# main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/method")
def request_type():
    return {"method": "GET"}

@app.post("/method")
def request_type():
    return {"method": "POST"}

@app.delete("/method")
def request_type():
    return {"method": "DELETE"}

@app.put("/method")
def request_type():
    return {"method": "PUT"}

class PatientRq(BaseModel):
    name: str
    surename: str

class PatientResp(BaseModel):
    id: int = 1
    patient: Dict

@app.post("/patient")
def create_patient(rq: PatientRq):
    return PatientResp(patient=rq.dict())

