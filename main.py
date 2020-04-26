# main.py

from fastapi import FastAPI, HTTPException, Cookie, Response, Depends
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
app.counter = 0

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/welcome")
def txt():
    return "no elo"


security = HTTPBasic()
@app.get("/login")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return {"username": credentials.username, "password": credentials.password}

