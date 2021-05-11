# from AudioAPI import db
import datetime

from dataclasses import dataclass
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


# class Song(db.Model):
#     __tablename__ = "filed_songs"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100))
#     duration = db.Column(db.Integer)
#     uploaded_time = db.Column(db.DateTime, default=datetime.datetime.now)
#
#
# class Podcast(db.Model):
#     __tablename__ = "filed_podcast"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100))
#     duration = db.Column(db.Integer)
#     uploaded_time = db.Column(db.DateTime, default=datetime.datetime.now)
#     host = db.Column(db.String(100))
#     participants = db.Column(db.String(100))
#
#
# class Audiobook(db.Model):
#     __tablename__ = "filed_audiobook"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100))
#     duration = db.Column(db.Integer)
#     uploaded_time = db.Column(db.DateTime, default=datetime.datetime.now)
#     author = db.Column(db.String(100))
#     narrator = db.Column(db.String(100))

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
    participants: str

    __tablename__ = "filed_podcast"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    duration = Column(Integer)
    uploaded_time = Column(DateTime, default=datetime.datetime.now)
    host = Column(String(100))
    participants = Column(String(100))


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
