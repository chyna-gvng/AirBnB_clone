#!/usr/bin/python3
"""
    Module that creates 'City' class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        Class to manage city objects
        Represent a city with a state id and a name
        Attributes:
            state_id (str): state id of the city
            name (str): name of the city
    """
    state_id = ""
    name = ""
