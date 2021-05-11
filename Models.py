# from AudioAPI import db
import datetime

from dataclasses import dataclass
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, JSON

Base = declarative_base()


@dataclass
class Song(Base):
    id: int
    title: str
    duration: int
    uploaded_time: datetime
    __tablename__ = "filed_songs"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    duration = Column(Integer)
    uploaded_time = Column(DateTime, default=datetime.datetime.now)


@dataclass
class Podcast(Base):
    id: int
    title: str
    duration: int
    uploaded_time: datetime
    host: str
    participants: list

    __tablename__ = "filed_podcast"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    duration = Column(Integer)
    uploaded_time = Column(DateTime, default=datetime.datetime.now)
    host = Column(String(100))
    participants = Column(JSON, nullable=True)


@dataclass
class Audiobook(Base):
    id: int
    title: str
    duration: int
    uploaded_time: datetime
    author: str
    narrator: str

    __tablename__ = "filed_audiobook"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    duration = Column(Integer)
    uploaded_time = Column(DateTime, default=datetime.datetime.now)
    author = Column(String(100))
    narrator = Column(String(100))
