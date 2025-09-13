#!/usr/bin/python3
"""
Module: file_storage
Defines FileStorage class to serialize and deserialize objects
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class_map = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}

class FileStorage:
    """Serializes instances to a JSON file and deserializes back"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Adds new object to __objects with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        json_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(json_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value["__class__"]
                    cls = class_map.get(cls_name)
                    if cls:
                        self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass