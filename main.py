# main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
app.counter = 0

class PatientRq(BaseModel):
    name: str
    surename: str

class PatientResp(BaseModel):
    id: str
    patient: dict


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get('/counter')
def counter():
    app.counter += 1
    return str(app.counter)

@app.post("/patient")
def create_patient(rq: PatientRq):
    app.counter += 1
    return PatientResp(id=str(app.counter), patient=rq.dict())

