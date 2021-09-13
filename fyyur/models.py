from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

venue_profiles = db.Table('venue_profiles',
    db.Column('venue_id', db.Integer, db.ForeignKey('venue.id')),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id')),
    db.UniqueConstraint('venue_id', 'genre_id'),
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

    # one-to-many relationship between Venue and Show
    shows = db.relationship('Show', backref='venue', lazy=True)

    # many-to-many relationship between Venue and Genre
    genres = db.relationship('Genre', secondary=venue_profiles, backref=db.backref('venue', lazy=True))

# class VenueSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Venue
#         shows = ma.auto_field()

# class VenueSchema(ma.SQLAlchemySchema):
#     class Meta:
#         model = Venue
#         shows = ma.auto_field()
    

artist_profiles = db.Table('artist_profiles',
    db.Column('artist_id', db.Integer, db.ForeignKey('artist.id')),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id')),
    db.UniqueConstraint('artist_id', 'genre_id')
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

    # one-to-many relationship Artist and Show | artist.show
    shows = db.relationship('Show', backref='artist', lazy=True)

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

    # one-to-many relationship with show as child | artist.show
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)

    # one-to-many relationship with Venue | venue.show
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)




    