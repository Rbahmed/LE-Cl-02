import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, request

engine = create_engine("postgresql://postgres:admin@localhost:5432/flight")
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html",flights=flights)

@app.route("/book", methods=["POST"])
def book():
    name= request.form.get("name")
    

    try:
        flight_id = int(request.form.get("flights_id"))
    except ValueError:
        render_template("error.html",message="Invelid flight number")

    if db.execute("SELECT * FROM flights WHERE id =:id",{"id": flight_id}).rowcount==0:
        render_template("error.html",message="No such a id with id")

    db.execute("INSERT INTO Passengers (passenger_name,flight_id) VALUES (:passenger_name,:flight_id)",
    {"passenger_name":name, "flight_id":flight_id})
    db.commit()
    return render_template("success.html")
