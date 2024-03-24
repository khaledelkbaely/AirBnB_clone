#!/usr/bin/python3
"""module for FileStorage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """class FileStorage"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return current instances"""
        return FileStorage().__objects

    def new(self, obj):
        """save new object in dictionary"""
        key = '{}.{}'.format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
        self.save()

    def save(self):
        """save obj as dict in file.json"""
        with open(FileStorage.__file_path, 'w') as jsonfile:
            json.dump(
                    {key: val.to_dict() for key, val in
                     FileStorage.__objects.items()}, jsonfile)

    def reload(self):
        """reload all instance in file.json"""
        from os import path
        if path.exists(FileStorage.__file_path):
            current_objects = {
                    'BaseModel': BaseModel,
                    'User': User,
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Place': Place,
                    'Review': Review
                    }
            with open(FileStorage.__file_path, 'r') as jsonfile:

                try:
                    dictionaries_of_object = json.load(jsonfile)
                except json.decoder.JSONDecodeError:
                    return

                FileStorage.__objects = {
                        k: current_objects[k.split('.')[0]](**v)
                        for k, v in dictionaries_of_object.items()}

    def show(self, key):
        """return current instance obj"""
        if key in FileStorage.__objects.keys():
            return FileStorage.__objects[key]
        else:
            return None

    def destroy(self, key):
        """delete obj"""
        if key in FileStorage.__objects.keys():
            del FileStorage.__objects[key]
            self.save()

    def exist(self, key):
        """check if obj exist"""
        if key in FileStorage.__objects.keys():
            return True
        else:
            return False

    def update(self, model, model_id, attribute, val):
        """update instance"""
        key = '{}.{}'.format(model, model_id)
        obj = FileStorage.__objects[key]

        val = eval(val)
        if obj:
            setattr(obj, attribute, val)
