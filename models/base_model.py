#!/usr/bin/python3
"""
    Define 'BaseModel' class
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
        Represent 'BaseModel'
    """

    def __init__(self, *args, **kwargs):
        """
            Initialize 'BaseModel' instance
            Args:
                *args (any): not used
                **kwargs (dict): key/value pairs of attributes
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """
            Update the public instance attribute 'updated_at'
            with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
            Return: dictionary of 'BaseModel' instance
            including key/value pair __class__ representing
            the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """
            Return: print/str representation of 'BaseModel' instance
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
