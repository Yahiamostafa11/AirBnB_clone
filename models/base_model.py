#!/usr/bin/python3
"""Module for BaseModel class by satamony"""
import uuid
from datetime import datetime



class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.created_at = datetime.strptime(args[i], '%Y-%m-%dT%H:%M:%S.%f')
                elif i == 2:
                    self.updated_at = datetime.strptime(args[i], '%Y-%m-%dT%H:%M:%S.%f')
                elif i == 3:
                    self.name = args[i]
                elif i == 4:
                    self.usrnumber = args[i]
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        return '[BaseModel] ({}) {}'.format(self.id, self.to_dict())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'usrnumber': self.usrnumber,
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def save(self):
        self.updated_at = datetime.now()

    

