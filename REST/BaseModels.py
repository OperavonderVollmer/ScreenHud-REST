from pydantic import BaseModel



class CityIdentifier(BaseModel):
    """
        Base model for cities
    """
    city: str = ""

class AlarmIdentifier(BaseModel):
    """
        Base model for alarms
    """
    title: str = ""

class ToggleIdentifier(BaseModel):
    """
        Base model for toggles
    """
    t: str = ""