#!/usr/bin/python3
"""
Contains class BaseModel
"""

from datetime import datetime
import models
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The BaseModel class from which future classes will be derived"""

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key in kwargs.keys():
                if key in ["created_at", "updated_at"]:
                    kwargs[key] = datetime.strptime(kwargs[key], time)
                    if key == "created_at":
                        self.created_at = kwargs["created_at"]
                    if key == "updated_at":
                        self.updated_at = kwargs["updated_at"]
                if "id" in kwargs.keys():
                    self.id = kwargs["id"]

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        dictionary = {"__class__": self.__class__.__name__, "id": self.id}
        if hasattr(self, "created_at")
            dictionary["created_at"] = self.created_at.isoformat()
        if hasattr(self, "updated_at")
            dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
