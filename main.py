# main.py

from fastapi import FastAPI, HTTPException, Cookie, Response, Depends, status, Request
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.responses import RedirectResponse, HTMLResponse
import secrets
from fastapi.templating import Jinja2Templates
from hashlib import sha256



app = FastAPI()
app.session_tokens = []
app.ID = 0
templates = Jinja2Templates(directory="templates")
app.secret_key = "very constant and random secret, best 64 characters, here it is."

@app.get("/")
def root():
    return {"message": "Hello World"}


security = HTTPBasic()

@app.get("/welcome")
def txt(request: Request, session_token: str = Cookie(None)):
    if session_token not in app.session_tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    return templates.TemplateResponse("item.html", {"request": request, "user": "trudnY"})



@app.post("/login")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "trudnY")
    correct_password = secrets.compare_digest(credentials.password, "PaC13Nt")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    session_token = sha256(bytes(f"{credentials.username}{credentials.password}{app.secret_key}", encoding='utf8')).hexdigest()
    app.session_tokens.append(session_token)
    response.set_cookie(key="session_token", value=session_token)
    response.headers["Location"] = "/welcome"
    response.status_code = status.HTTP_302_FOUND





@app.post("/logout")
def logout(* , response: Response, session_token: str = Cookie(None)):
    if session_token not in app.session_tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    app.session_tokens.remove(session_token)
    response = RedirectResponse(url='/')
    return response