#!/usr/bin/python3
"""File Storage Module
This module stores and reloads objects of
class 'Basemodel' or it's sub classes.
"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import path


class FileStorage:
    """FileStorage Class
    The class serialize and deserialize instances.
    Attributes:
        __file_path (str): This is the path of the JSON file in which
            the contents of the `__objects` variable will be stored.
        __objects (dict): This store all the instances data
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key_name = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key_name] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_object = {}
        for key, obj in self.__objects.items():
            json_object[key] = obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(json_object, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                json_object = json.load(file)

            for key in json_object.keys():
                class_name = json_object[key]["__class__"]
                object_dict = json_object[key]
                self.__objects[key] = eval(class_name)(**object_dict)
