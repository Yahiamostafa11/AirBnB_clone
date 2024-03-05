#!/usr/bin/python3
"""Module for BaseModel class by satamony"""
import uuid
from datetime import datetime
import json


class BaseModel:
    def __init__(self, name, my_number):
        self.id = str(uuid.uuid4())
        self.name = name
        self.my_number = my_number
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        return '[BaseModel] ({}) {}'.format(self.id, self.to_dict())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'my_number': self.my_number,
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def save(self):
        self.updated_at = datetime.now()

    def to_json(self):
        return json.dumps(self.to_dict(), default=str)

