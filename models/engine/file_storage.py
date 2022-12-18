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
        if os.path.isfile("file.json"):
            with open(FileStorage.__fil_path) as file:
                obj_dict = json.load(file)
                
