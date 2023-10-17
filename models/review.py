#!/usr/bin/python3
"""Defines the Review class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class inherited from BaseModel.
    Represents a review for a place.
    """

    text: str = ""
    user_id: str = "" 
    place_id: str = ""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize a Review object"""
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        """Return string representation"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
