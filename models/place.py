#!/usr/bin/python3
"""
    Define 'Place' class
"""
from models.base_model import BaseModel


class Place(BaseModel):

    """
        Class to manage place objects
        Represent a place with a city id, user id, name, description,
        number of rooms, number of bathrooms, maximum number of guests,
        price by night, latitude, longitude and a list of amenity ids
        Attributes:
            city_id (str): city's id
            user_id (str): user's id
            name (str): name of the place.
            description (str): a description of the place
            number_rooms (int): number of rooms of the place
            number_bathrooms (int): number of bathrooms of the place
            max_guest (int): maximum number of guests of the place
            price_by_night (int): price per nght of the place
            latitude (float): latitude of the place
            longitude (float): longitude of the place
            amenity_ids (list): list of Amenity IDs associated with the place
        """

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
