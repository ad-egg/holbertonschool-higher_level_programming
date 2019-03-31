#!/usr/bin/python3
"""the class definition of a State an an instance Base = declarative_base()"""


from model_state import State
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """a class that inherits from Base"""
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
