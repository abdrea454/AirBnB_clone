#!/usr/bin/python3
"""Place class definition"""

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Place class.

    Attributes:
        city_id (str): City ID.
        user_id (str): User ID. 
        name (str): Name of place.
        description (str): Description.
        number_rooms (int): Number of rooms.
        number_bathrooms (int): Number of bathrooms.
        max_guest (int): Max number of guests.
        price_by_night (int): Price per night in cents.
        latitude (float): Latitude.
        longitude (float): Longitude.
        amenity_ids (List[str]): Amenity IDs.
    """

    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: List[str] = []

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
