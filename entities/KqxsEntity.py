import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()

class KqxsEntity(Base):
    __tablename__ = 'kqxs'
    id = Column(Integer, primary_key=True)
    place = Column(String(256))
    dayOfWeek = Column(Integer)
    db = Column(String(20))
    g1 = Column(String(20))
    g21 = Column(String(20))
    g22 = Column(String(20))
    g31 = Column(String(20))
    g32 = Column(String(20))
    g33 = Column(String(20))
    g34 = Column(String(20))
    g35 = Column(String(20))
    g36 = Column(String(20))
    g41 = Column(String(20))
    g42 = Column(String(20))
    g43 = Column(String(20))
    g44 = Column(String(20))
    g51 = Column(String(20))
    g52 = Column(String(20))
    g53 = Column(String(20))
    g54 = Column(String(20))
    g55 = Column(String(20))
    g56 = Column(String(20))
    g61 = Column(String(20))
    g62 = Column(String(20))
    g63 = Column(String(20))
    g71 = Column(String(20))
    g72 = Column(String(20))
    g73 = Column(String(20))
    g74 = Column(String(20))
    tail1 = Column(String(20))
    tail2 = Column(String(20))
    tail3 = Column(String(20))
    tail4 = Column(String(20))
    tail5 = Column(String(20))
    tail6 = Column(String(20))
    tail7 = Column(String(20))
    tail8 = Column(String(20))
    tail9 = Column(String(20))
    date = Column(TIMESTAMP)
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')
engine = create_engine('postgresql://kl:1@localhost:5432/xskt')
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)