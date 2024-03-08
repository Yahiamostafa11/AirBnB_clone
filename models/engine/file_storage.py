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
    __file_path = 'file.json'
    __objects = {}

    classes = {
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w") as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()},
                f
            )

    def reload(self):
        try:
            with open(FileStorage.__file_path) as f:
                data = json.load(f)
                for k, v in data.items():
                    class_name = v.get("__class__")
                    if class_name:
                        del v["__class__"]
                        self.new(globals()[class_name](**v))
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass

    def destroy(self, obj=None):
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            del FileStorage.__objects[key]
            FileStorage.save()

    def delete(self, obj=None):
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            del FileStorage.__objects[key]
            FileStorage.save()

    def close(self):
        FileStorage.reload()
