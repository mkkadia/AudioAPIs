from AudioAPI import db


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    uploaded_time = db.Column(db.Datetime)


class Podcast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    uploaded_time = db.Column(db.Datetime)
    host = db.Column(db.String(100))
    participants = db.Column(db.String(100))


class Audiobook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    uploaded_time = db.Column(db.Datetime)
    author = db.Column(db.String(100))
    narrator = db.Column(db.String(100))
