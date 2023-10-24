#!/usr/bin/python3
"""
Python file similar to model_state.py named model_city.py 
that contains the class definition of a City
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

class City(Base):
    """city representation"""
    __tablename__ = "cities"
    id = column(Integer, primary_key=true)
    name = column(string(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))