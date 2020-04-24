import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import csv

engine = create_engine("postgresql://postgres:admin@localhost:5432/flight")
db = scoped_session(sessionmaker(bind=engine))


def main():
    f = open("flight.csv")
    reder = csv.reader(f)
    for origin,destination,duration in reder:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
                    {"origin":origin, "destination":destination, "duration": duration})
        print (f"Added origin {origin} destination {destination} and duration {duration}")
    db.commit()


if __name__ == "__main__":
    main()
