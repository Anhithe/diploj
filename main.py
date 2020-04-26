# main.py

from fastapi import FastAPI, HTTPException, Cookie, Response
from pydantic import BaseModel

app = FastAPI()
app.counter = 0
app.secret_key = "very constant and random secret, best 64 characters"

class PatientRq(BaseModel):
    name: str
    surename: str

class PatientResp(BaseModel):
    id: str
    patient: dict


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get('/num/{p}')
def counter(p):
    return str(p)

@app.get("/welcome")
def txt():
    return "no elo"

@app.post("/patient")
def create_patient(rq: PatientRq):
    app.counter += 1
    return PatientResp(id=str(app.counter), patient=rq.dict())

@app.get("/patient/{pk}")
def patient_finder(pk):
    if int(pk) > app.counter:
        raise HTTPException(status_code=204, detail="No content")
    return PatientRq(name="NAME", surename="SURENAME")


