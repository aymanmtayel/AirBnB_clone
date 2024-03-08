#!/usr/bin/env python3
#base class for the AirBnb project

from datetime import datetime
import uuid

class BaseModel:
    """the base class for all of our models"""
    def __init__(self, *args, **kwargs):
        """our base model constructor"""
        if kwargs:
            kwargs.pop('__class__', None)
            if "created_at" in kwargs:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            if "updated_at" in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")

            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """returns the representation of the class"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"


    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
