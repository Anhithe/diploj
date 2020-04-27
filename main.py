# main.py

from fastapi import FastAPI, HTTPException, Cookie, Response, Depends, status
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.responses import RedirectResponse
import secrets

app = FastAPI()
app.counter = 0

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/welcome")
def txt():
    return "no elo"


security = HTTPBasic()


@app.post("/login")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "trudnY")
    correct_password = secrets.compare_digest(credentials.password, "PaC13Nt")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    response = RedirectResponse(url='/welcome')
    return response

@app.post("/logout")
    response = RedirectResponse(url='/')
    return response