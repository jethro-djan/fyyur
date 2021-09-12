import json
import dateutil.parser
# import babel
from flask import (
  render_template, request, Response, flash, redirect, url_for, Blueprint
)

import logging
from logging import Formatter, FileHandler, disable
from .forms import *


# from fyyur.form import create_form
from fyyur.models import Venue, Artist
from fyyur.forms import ShowForm, VenueForm, ArtistForm

form = Blueprint('forms', __name__, template_folder='templates')

@form.route('/venues/create', methods=['GET', 'POST'])
def create_venue_form():
  form = VenueForm()
  if form.validate_on_submit():
    name = Venue.query.filter_by(name=form.name.data).first()
    if name is None:
      name = Venue(name=form.name.data)
      city = Venue(city=form.city.data)
      state = Venue(state=form.state.data)
      address = Venue(address=form.address.data)
      phone = Venue(phone=form.phone.data)
      if phone == '':
        phone = None 
      facebook_link = Venue(facebook_link=form.facebook_link.data)
      if facebook_link == '':
        facebook_link = None
      image_link = Venue(image_link=form.image_link.data)
      if image_link == '':
        image_link = None 
      genres = Venue(genres=form.genres.data)
      seeking_talent = Venue(seeking_talent=form.seeking_talent.data)
      # if seeking_talent == False:
      #   form.seeking_description(disabled=True)
      seeking_description = Venue(seeking_description=form.seeking_description.data)
      
  return render_template('forms/new_venue.html', form=form)

@form.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistForm()
  artist={
    "id": 4,
    "name": "Guns N Petals",
    "genres": ["Rock n Roll"],
    "city": "San Francisco",
    "state": "CA",
    "phone": "326-123-5000",
    "website": "https://www.gunsnpetalsband.com",
    "facebook_link": "https://www.facebook.com/GunsNPetals",
    "seeking_venue": True,
    "seeking_description": "Looking for shows to perform at in the San Francisco Bay Area!",
    "image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80"
  }
  # TODO: populate form with fields from artist with ID <artist_id>
  return render_template('forms/edit_artist.html', form=form, artist=artist)

@form.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm()
  venue={
    "id": 1,
    "name": "The Musical Hop",
    "genres": ["Jazz", "Reggae", "Swing", "Classical", "Folk"],
    "address": "1015 Folsom Street",
    "city": "San Francisco",
    "state": "CA",
    "phone": "123-123-1234",
    "website": "https://www.themusicalhop.com",
    "facebook_link": "https://www.facebook.com/TheMusicalHop",
    "seeking_talent": True,
    "seeking_description": "We are on the lookout for a local artist to play every two weeks. Please call us.",
    "image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60"
  }
  # TODO: populate form with values from venue with ID <venue_id>
  return render_template('forms/edit_venue.html', form=form, venue=venue)

@form.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@form.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)