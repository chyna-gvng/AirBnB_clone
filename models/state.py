#!/usr/bin/python3
"""
    Define 'State' class
"""
from models.base_model import BaseModel


class State(BaseModel):

    """
        Class to manage state objects
        Represent a state with a name
        Attributes:
            name (str): The name of the state
    """

    name = ""
