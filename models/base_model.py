#!/usr/bin/python3

"""Defines BaseModel class"""

import uuid
from datetime import datetime

class BaseModel:

    """Base model for all models in project"""

    id: str
    created_at: datetime
    updated_at: datetime

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    @classmethod
    def from_dict(cls, d: dict) -> 'BaseModel':
        """Create instance from dictionary"""
        if "__class__" in d:
            d.pop("__class__")
        d["created_at"] = datetime.fromisoformat(d["created_at"])
        d["updated_at"] = datetime.fromisoformat(d["updated_at"])
        return cls(**d)

    def __str__(self) -> str:
        """Return string representation"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """Update updated_at time"""
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """Convert to dictionary"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = type(self).__name__
        dict_copy['created_at'] = dict_copy['created_at'].isoformat()
        dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()
        return dict_copy
