"""File storage module"""

import json
import os

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City 
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:
    """Serializes and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets obj in __objects with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        json_objects = {}
        for key, val in self.__objects.items():
            json_objects[key] = val.to_dict()
        
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    self.__objects[key] = eval(val["__class__"])(**val)
        except FileNotFoundError:
            pass
