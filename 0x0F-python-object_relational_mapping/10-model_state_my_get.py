#!/usr/bin/python3
# 10-model_state_my_get.py
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

    state = session.query(State).filter(State.name == argv[4])

    if state.count() == 0:
        print("Not found")

    else:
        for i in state:
            print('{}'.format(i.id))

    session.close()
