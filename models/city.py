#!/usr/bin/python3
"""City class definition"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    City class.
   
    Attributes:
        state_id (str): State ID.
        name (str): Name of the city. 
    """
    
    state_id: str = ""
    name: str = ""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
