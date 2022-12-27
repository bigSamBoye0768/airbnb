#!/usr/bin/python3
import json
import os

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """Returns all objects as a dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file""" 
        with open(FileStorage.__file_path, 'w') as file:
            d = {k:v.to_dict() for k,v in FileStorage.__objects.items()}
            json.dump(d, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review
        dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'City': City, 'Amenity': Amenity, 'State': State,
               'Review': Review}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(dct[value['__class__']](**value))
                
                                                                     