import sqlite3
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.on_event("startup")
async def startup():
    app.db_connection = sqlite3.connect('chinook.db')


@app.on_event("shutdown")
async def shutdown():
    app.db_connection.close()


@app.get("/tracks/composers/{composer_name}")
async def composer(composer_name: str):
    tracks = app.db_connection.execute("SELECT Name FROM tracks WHERE Composer LIKE ? ORDER BY Name", ("%"+composer_name+"%", )).fetchall()
    if not tracks:
        raise HTTPException(status_code=404, detail="error")
    return tracks
