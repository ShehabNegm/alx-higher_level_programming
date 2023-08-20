#!/usr/bin/python3
# 14-model_city_fetch_by_state.py
"""import a model and fitch its results"""

from sys import argv
from model_state import Base, State
from model_city import City
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

    for c, s in session.query(
        City, State).filter(
            City.state_id == State.id).order_by(City.id).all():
        print('{}: ({}) {}'.format(s.name, c.id, c.name))
