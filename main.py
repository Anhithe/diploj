import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Album(BaseModel):
    title: str
    artist_id: int


class Customer(BaseModel):
    company: str
    address: str
    city: str
    state: str
    country: str
    postalcode: str
    fax: str


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
    tracks = cursor.execute("SELECT Name FROM tracks WHERE Composer LIKE ? ORDER BY Name",
                            ("%" + composer_name + "%",)).fetchall()
    if not tracks:
        raise HTTPException(status_code=404, detail="error")
    return tracks


@app.post("/albums/", status_code=201)
async def albums_add(album: Album):
    checker = app.db_connection.execute("SELECT ArtistId FROM artists WHERE ArtistId = ?",
                                        (album.artist_id,)).fetchone()
    if not checker:
        raise HTTPException(status_code=404, detail="error")
    cursor = app.db_connection.execute(
        "INSERT INTO albums (Title, ArtistId) VALUES (?, ?)", (album.title, album.artist_id)
    )
    app.db_connection.commit()
    new_album_id = cursor.lastrowid
    app.db_connection.row_factory = sqlite3.Row
    album = app.db_connection.execute("SELECT * FROM albums WHERE AlbumId = ?", (new_album_id,)).fetchone()
    return album


@app.get("/albums/{album_id}", status_code=200)
async def album_getter(album_id: int):
    cursor = app.db_connection.cursor()
    app.db_connection.row_factory = lambda cursor, x: x[0]
    album1 = cursor.execute("SELECT * FROM albums WHERE AlbumId = ?", (album_id,)).fetchone()
    return album1


import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Album(BaseModel):
    title: str
    artist_id: int


class Customer(BaseModel):
    company: str = None
    address: str = None
    city: str = None
    state: str = None
    country: str = None
    postalcode: str = None
    fax: str = None


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
    tracks = cursor.execute("SELECT Name FROM tracks WHERE Composer LIKE ? ORDER BY Name",
                            ("%" + composer_name + "%",)).fetchall()
    if not tracks:
        raise HTTPException(status_code=404, detail="error")
    return tracks


@app.post("/albums/", status_code=201)
async def albums_add(album: Album):
    checker = app.db_connection.execute("SELECT ArtistId FROM artists WHERE ArtistId = ?",
                                        (album.artist_id,)).fetchone()
    if not checker:
        raise HTTPException(status_code=404, detail="error")
    cursor = app.db_connection.execute(
        "INSERT INTO albums (Title, ArtistId) VALUES (?, ?)", (album.title, album.artist_id)
    )
    app.db_connection.commit()
    new_album_id = cursor.lastrowid
    app.db_connection.row_factory = sqlite3.Row
    album = app.db_connection.execute("SELECT * FROM albums WHERE AlbumId = ?", (new_album_id,)).fetchone()
    return album


@app.get("/albums/{album_id}", status_code=200)
async def album_getter(album_id: int):
    cursor = app.db_connection.cursor()
    app.db_connection.row_factory = lambda cursor, x: x[0]
    album1 = cursor.execute("SELECT * FROM albums WHERE AlbumId = ?", (album_id,)).fetchone()
    return album1


@app.put("/customers/{customer_id}", status_code=200)
async def putter(customer_id: int, customer: Customer):
    checker = app.db_connection.execute("SELECT CustomerId FROM customers WHERE CustomerId = ?",
                                        (customer_id,)).fetchone()
    if not checker:
        raise HTTPException(status_code=404, detail="error")
    if customer.company:
        cursor = app.db_connection.execute("UPDATE Customers SET company = ? WHERE CustomerId = ?",
                                       (customer.company, customer_id))
    if customer.address:
        cursor = app.db_connection.execute("UPDATE Customers SET address = ? WHERE CustomerId = ?",
                                       (customer.address, customer_id))
    if customer.city:
        cursor = app.db_connection.execute("UPDATE Customers SET city = ? WHERE CustomerId = ?",
                                       (customer.city, customer_id))
    if customer.state:
        cursor = app.db_connection.execute("UPDATE Customers SET state = ? WHERE CustomerId = ?",
                                       (customer.state, customer_id))
    if customer.country:
        cursor = app.db_connection.execute("UPDATE Customers SET country = ? WHERE CustomerId = ?",
                                       (customer.country, customer_id))
    if customer.postalcode:
        cursor = app.db_connection.execute("UPDATE Customers SET postalcode = ? WHERE CustomerId = ?",
                                       (customer.postalcode, customer_id))
    if customer.fax:
        cursor = app.db_connection.execute("UPDATE Customers SET fax = ? WHERE CustomerId = ?",
                                       (customer.fax, customer_id))
    app.db_connection.commit()

    app.db_connection.row_factory = sqlite3.Row
    stored_customer_data = app.db_connection.execute("SELECT * FROM customers WHERE CustomerId = ?",
                                                     (customer_id,)).fetchone()
    return stored_customer_data
