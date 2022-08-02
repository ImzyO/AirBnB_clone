#!/usr/bin/python3
"""module for base_model.py"""

from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    class BaseModel: defines all common methods/attributes
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """initialization of public instance attributes"""
        # If only args;
        # id is assigned a random value by generating uuid.uuid4 as a string
        # created_at is assigned with the current datetime using a
        # datetime oject .now which is preferrable to(.utcnow & today)
        # updated_at is assigned with the current datetime and is updated
        # everytime an oject is changed

        # else if kwargs;
        # id is the value inputed which is kwargs
        # created_at returns corresponding datestring passed according to
        # format using datetime object .strptime same as updated_at

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            self.id = kwargs
            self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:./
            %MM:S.%f"
            self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:./
            %MM:S.%f"

        def __str__(self):
            """prints string representations"""
            """self.__class__.__name__ refers to calling class name"""
            return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

        def save(self):
            """
            updates the public instance attribute updated_at with 
            the current datetime
            """
            self.updated_at = datetime.now()

        def to_dict(self):
            """
            returns a dictionary containing all keys/values of __dict__
            of the instance
            """
            # by using self.__dict__, only instance attributes set
            # will be returned.
            # a key __class__ must be added to this dictionary with
            # the class name of the object.
            # created_at and updated_at must be converted to string object 
            # in ISO format;
            # format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
            # using the .isoformat object from datetime.
            # a copy is created to not modify original dict

            x = self.__dict__.copy()
            x["__class__"] = self.__class__.__name__
            x["created_at"] = self.created_at.isoformat()
            x["updated_at"] = self.updated_at.isoformat()

            return x
