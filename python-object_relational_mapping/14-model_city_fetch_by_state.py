#!/usr/bin/python3

"""
    this is a script that prints all City objects
    from the database hbtn_0e_14_usa
"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    cities = session.query(State, City).filter(State.id == City.state_id)

    for citie in cities:
        print("{}: ({}) {}".format(citie.State.name, citie.City.id, citie.City.name))

    session.close()
