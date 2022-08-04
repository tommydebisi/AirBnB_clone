#!/usr/bin/python3
"""
    File storage module
"""
import json as js


class FileStorage:
    """
        File Storage Class
    """

    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """
            returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id

            Args:
                obj: object to be saved
        """
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """
            serializes __objects to the JSON file
        """
        new_dict = dict()
        for key, val in self.__objects.items():
            new_dict[key] = val.to_dict()

        with open(self.__file_path, 'w', encoding="utf-8") as filename:
            js.dump(new_dict, filename)

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        from models.base_model import BaseModel

        try:
            with open(self.__file_path, encoding="utf-8") as filename:
                stored_obj = js.load(filename)

            for key, val in stored_obj.items():
                self.__objects[key] = BaseModel(**val)
        except Exception:
            pass
