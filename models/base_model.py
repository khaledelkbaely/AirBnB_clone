#!/usr/bin/python3
"""module for BaseModel"""
import models
import uuid
from datetime import datetime


class BaseModel():
    """class BaseModel"""

    def __init__(self, *args, **kwargs):
        """constructor"""
        if kwargs:
            for key, val in kwargs.items():
                if key not in ('__class__', 'created_at', 'updated_at'):
                    self.__dict__[key] = val
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """return string representaion of instance"""
        s = '[{}] ({}) {}'
        return s.format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """sace instance"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """return dict representaion of instance"""
        new_dict = dict()

        new_dict['__class__'] = type(self).__name__
        new_dict.update(self.__dict__)
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()

        return new_dict
