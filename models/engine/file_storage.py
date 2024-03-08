#!/usr/bin/env python3
#file sotrage module to create, save and read json files.

import json

class FileStorage:
    """
    class of file storage at which our console will
    be able to save delete and add and read JSon files
    """
    def __init__(self):
        self.__objects = []
        self.__file_path = "file.json"

    def all(self):
        return (self.__objects)

    def new(self, obj):


