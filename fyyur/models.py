from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()

venue_profiles = db.Table('venue_profiles',
    db.Column('venue_id', db.Integer, db.ForeignKey('artist.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primary_key=True)
)

class Venue(db.Model):
    # __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))

    # show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable=False)
    artists = db.relationship('Artist', backref='venue', lazy=True)
    show = db.relationship('Show', backref='venue', uselist=False)
    genres = db.relationship('Genre', secondary=venue_profiles, lazy='subquery', backref=db.backref('venues', lazy=True))
    

artist_profiles = db.Table('artist_profiles',
    db.Column('artist_id', db.Integer, db.ForeignKey('artist.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primary_key=True)
)

class Artist(db.Model):
    # __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))

    # venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)

    genres = db.relationship('Genre', secondary=artist_profiles, lazy='subquery', backref=db.backref('artists', lazy=True))



class Genre(db.Model):
    # __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    # venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)


class Show(db.Model):
    # __tablename__ = 'shows'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    # future_show = db.Column(db.Boolean, nullable=False, default=True)

    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))

    artist = db.relationship('Artist')




    