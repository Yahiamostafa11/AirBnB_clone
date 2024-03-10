#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State


class FileStorage:
    """FileStorage class that serial
    izes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method to return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Method to set in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Method to serialize __objects to the JSON file (path:__file_path)"""
        new_dict = {}
        for k, v in self.__objects.items():
            new_dict[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Method to deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                new_dict = json.load(f)
                for k, v in new_dict.items():
                    cls_name = v["__class__"]
                    self.__objects[k] = eval(cls_name)(**v)
        except FileNotFoundError:
            pass
