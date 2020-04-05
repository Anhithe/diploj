# main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
app.counter = 1
class PatientRq(BaseModel):
    name: str
    surename: str

class PatientResp(BaseModel):
    id: int
    patient: dict


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/patient")
def create_patient(rq: PatientRq):
    return PatientResp(id=app.counter, patient=rq.dict())


app.counter += 1

