#!/usr/bin/python3
"""the class definition of a State and an instance Base = declarative_base()"""


from sqlalchemy import Table, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """a class that inherits from Base"""
    __tablename__ = "states"
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
