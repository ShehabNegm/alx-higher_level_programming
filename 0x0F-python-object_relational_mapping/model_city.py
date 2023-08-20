#!/usr/bin/python3
# model_city.py
""" define city class """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey

Base = declarative_base()


class City(Base):
    """class city"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True,
                unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey(State.id))
