#!/usr/bin/python3
"""Creates sql object state"""


from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

metaData = MetaData()
Base = declarative_base(metadata=metaData)


class State(Base):
    """
    class with id and name column
    """
    __tablename__ = "states"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
