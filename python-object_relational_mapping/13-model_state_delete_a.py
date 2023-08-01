#!/usr/bin/python3

"""
This is  a script that deletes all State objects
with a name containing the letter a from the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    delete_state = session.query(State).filter(State.name.ilike("%a%")).all()

    for state in delete_state:
        session.delete(state)

    session.commit()

    session.close()
