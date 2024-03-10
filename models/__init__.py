#!/usr/bin/python3
"""__init__  method for models directory """

from models.engine.file_storage import FileStorage

"""Create a unique FileStorage instance for the application"""
storage = FileStorage()
"""Call the reload method on the storage instance"""
storage.reload()
