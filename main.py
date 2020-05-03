import sqlite3
from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def startup():
    app.db_connection = sqlite3.connect('chinook.db')


@app.on_event("shutdown")
async def shutdown():
    app.db_connection.close()


@app.get("/tracks", status_code=200)
async def tracker(page: int = 0, per_page: int = 10):
    page = page*per_page
    app.db_connection.row_factory = sqlite3.Row
    tracks = app.db_connection.execute(
        "SELECT * FROM tracks ORDER BY TrackId LIMIT :per_page OFFSET :page",
        {'per_page': per_page, 'page': page}).fetchall()
    return tracks


@app.get("/tracks/{page}/{per_page}", status_code=200)
async def tracker(page: int = 0, per_page: int = 10):
    page = page*per_page
    app.db_connection.row_factory = sqlite3.Row
    tracks = app.db_connection.execute(
        "SELECT * FROM tracks ORDER BY TrackId LIMIT :per_page OFFSET :page",
        {'per_page': per_page, 'page': page}).fetchall()
    return tracks
