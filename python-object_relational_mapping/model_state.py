#!/usr/bin/python3
# Creates a State class that maps to the 'states' table in MySQL.
# Inherits from SQLAlchemy's Base.

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class that represents a row in the 'states' table.

    __tablename__ (str): sets the table name to 'states'.
    id (sqlalchemy.Integer): unique ID for each state.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
