#!/usr/bin/python3
"""base_model module
This module contains all a class which is used by all the
classes of the AirBnB projects.
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """ BaseModel class
    This is the Base Model that takes care of the
    initialization, serialization and deserialization
    of instances.

    Attributes:
        id (str): It's a UUID for the instance created.
        created_at (datetime): The current date and time that
            an instance is created.
        updated_at (datetime): The current date and time that
            an instance is created and it will be updated every
            time that the object changes.
    """
    def __init__(self, *args, **kwargs):
        """BaseModel __init__ Method
        The BaseModel class from which future classes will be derived
        """

        if kwargs:
            tdf = "%Y-%m-%dT%H:%M:%S.%f"
            for key in kwargs.keys():
                if key in ["created_at", "updated_at"]:
                    kwargs[key] = datetime.strptime(kwargs[key], tdf)

                self.id = kwargs["id"]
                self.created_at = kwargs["created_at"]
                self.updated_at = kwargs["updated_at"]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of BaseModel instances"""

        x = self.__class__.__name__
        y = self.id
        z = self.__dict__

        return "[{:s}] ({:s}) {}".format(x, y, z)

    def save(self):
        """Updates and saves a Basemodel instance
        Updates:
            It updates `updated_at` attribute
            with the current datetime

        Save:
            It dumps the class data
            into a jason file
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Converts the information of the class to human-readable format
        Returns a new dictionary containing all keys/values
        of __dict__ of the instance.
        """
        dictionary = {"__class__": self.__class__.__name__, "id": self.id}
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
