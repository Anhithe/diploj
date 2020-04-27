# main.py

from fastapi import FastAPI, HTTPException, Cookie, Response, Depends, status, Request
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.responses import RedirectResponse
import secrets
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def root():
    return {"message": "Hello World"}


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

@app.get("/welcome")
def txt(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "trudnY")
    correct_password = secrets.compare_digest(credentials.password, "PaC13Nt")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return templates.TemplateResponse("item.html", {"request": request, "my_string": "trudnY"})




@app.post("/logout")
def logout():
    response = RedirectResponse(url='/')
    return response