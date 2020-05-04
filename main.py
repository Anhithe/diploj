import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Album(BaseModel):
    title: str
    artist_id: int


@app.on_event("startup")
async def startup():
    app.db_connection = sqlite3.connect('chinook.db')


@app.on_event("shutdown")
async def shutdown():
    app.db_connection.close()


@app.get("/tracks/composers/")
async def composer(composer_name: str):
    cursor = app.db_connection.cursor()
    app.db_connection.row_factory = lambda cursor, x: x[0]
    tracks = cursor.execute("SELECT Name FROM tracks WHERE Composer LIKE ? ORDER BY Name", ("%"+composer_name+"%", )).fetchall()
    if not tracks:
        raise HTTPException(status_code=404, detail="error")
    return tracks


@app.post("/albums", status_code=201)
async def albums_add(album: Album):
    cursor = app.db_connection.execute(
        "INSERT INTO albums (Title, ArtistId) VALUES (?, ?)", (album.title, album.artist_id)
    )
    if not album.title or album.artist_id:
        raise HTTPException(status_code=404, detail="error")
    app.db_connection.commit()
    new_album_id = cursor.lastrowid
    app.db_connection.row_factory = sqlite3.Row
    album = app.db_connection.execute("SELECT * FROM albums WHERE AlbumId = ?", (new_album_id,)).fetchone()
    return album

