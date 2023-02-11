#!/usr/bin/python3
"""
    Defines 'Review' class.
"""
from models.base_model import BaseModel


class Review(BaseModel):

    """
        Class to manage review objects
        Represent a review with a place id, user id and text
        Attributes:
            place_id (str): place's id
            user_id (str): user's id
            text (str): text of the review
    """

    place_id = ""
    user_id = ""
    text = ""
