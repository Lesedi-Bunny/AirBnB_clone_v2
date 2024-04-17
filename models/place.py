#!/usr/bin/python3

""" Place Module for HBNB project """
from models.base_model import BaseModel
import uuid


class Place(BaseModel):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        initilalize place objects
        using Base model as parent class
        """
        super().__init__(*args, **kwargs)
        if 'id' not in kwargs:
            self.id = kwargs.get('id', str(uuid.uuid4()))
