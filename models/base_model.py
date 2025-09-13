#!/usr/bin/python3
"""
Module: base_model
Defines the BaseModel class for AirBnB clone
"""

import uuid
from datetime import datetime


class BaseModel:
    """BaseModel defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """
        Initialization of the BaseModel instance.
        If kwargs is not empty, set attributes from the dictionary,
        otherwise create new id, created_at and updated_at.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":  # Skip __class__
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage  # Import here to avoid circular import
            storage.new(self)  # Add instance to storage

    def __str__(self):
        """Return string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime and saves to storage"""
        self.updated_at = datetime.now()
        from models import storage  # Import here to avoid circular import
        storage.save()  # Save changes to storage

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__.
        Adds __class__ key with the class name.
        Converts datetime attributes to ISO format string.
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        if "created_at" in dict_copy:
            dict_copy["created_at"] = self.created_at.isoformat()
        if "updated_at" in dict_copy:
            dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy