from pydantic import BaseModel



class City(BaseModel):
    """
        Base model for cities
    """
    city: str = ""