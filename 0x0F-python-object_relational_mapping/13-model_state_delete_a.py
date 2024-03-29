#!/usr/bin/python3
# 13-model_state_delete_a.py
"""import a model and fitch the states where it has letetr a"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format
        (argv[1],
         argv[2],
         argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for states in session.query(State).filter(State.name.like('%a%')):
        session.delete(states)
    session.commit()
    session.close()
