#!/usr/bin/python3
"""Module for BaseModel class by satamony"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

            models.storage.new(self)

    def __str__(self):
        return '[self.class.name] ({}) {}'.format(self.id, self.dict())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()
