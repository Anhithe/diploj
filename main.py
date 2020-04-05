# main.py

from fastapi import FastAPI

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