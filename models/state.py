#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import uuid


class State(BaseModel):
    """ State class """

    def __init__(self, *args, **kwargs):
        """
        Ensure Base model constructor is called
        when a state object is initialized
        """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get("name", )
        # add id explicitly
        if 'id' not in kwargs:
            self.id = kwargs.get('id', str(uuid.uuid4()))
