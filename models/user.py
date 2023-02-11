#!/usr/bin/python3
"""
    Define 'User' class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        Class to manage user objects
        Represent user with an email, password, first name and last name
        Attributes:
            email (str): user's email
            password (str): user's password
            first_name (str): user's first name
            last_name (str): user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
