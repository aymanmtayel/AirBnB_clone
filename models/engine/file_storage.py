#!/usr/bin/env python3
#file sotrage module to create, save and read json files.

import json

class FileStorage:
    """
    class of file storage at which our console will
    be able to save delete and add and read JSon files
    """
    __objects = {}
    __file_path = "file.json"

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        print(json_dict)
        with open(self.__file_path, "w") as file:
            json.dump(json_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                json_dict = json.load(file)
                for key, value in json_dict.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(e)
            pass