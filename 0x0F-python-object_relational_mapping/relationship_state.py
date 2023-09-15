#!/usr/bin/python3
# Graham S. Paul (relationship_state.py)
"""
Explains class State
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# from relationship_city import City

Base = declarative_base()


class State(Base):
    """
    Class State; Examples of Base
    Joined to MySQL table "states"
    """
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
