#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    types = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }

    def all(self, cls=None):
        """Returns a dictionary of models currently in a spesific class"""
        if cls is None:
            return FileStorage.__objects
        else:
            temp = {}
            for key, val in FileStorage.__objects.items():
                if isinstance(val, cls):
                    temp[key] = val
            return temp

    def new(self, obj):
        """Adds new object to storage dictionary"""
        FileStorage.__objects.update(
            {obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""

        classes = FileStorage.types
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    FileStorage.__objects[key] = classes[val['__class__']](
                        **val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside"""
        if obj is None:
            return
        key = f"{obj.__class__.__name__}.{obj.id}"
        if key in self.__objects:
            del self.__objects[key]
            self.save()

    def get(self, cls, id):
        """This method retive one object
            Args:
                cls - desired class to look for
                id - id of the targeted object
            Returns:
                The object with set id if found
        """

        if cls in FileStorage.types:
            targets = self.all(cls)
            for key, value in targets.items():
                try:
                    className, classId = key.split('.')
                except:
                    pass
                if classId == id:
                    return value
            return None
        else:
            return None

    def count(self, cls=None):
        """This method counts the number of objects in storage
            Args:
                cls - desired class to count(OPTIONAL)
            Returns:
                The number of classes found within storage
        """

        count = 0
        if cls in FileStorage.types:
            lista = self.all(cls)
            for element in lista:
                count += 1
        return count


        
