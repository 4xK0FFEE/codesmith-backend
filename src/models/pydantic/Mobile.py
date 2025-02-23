from src.models.pydantic import General

class Mobile(General):
    authentication: str
    framework: str
    navigation: str
    stateManagement: str
    storage: str

__all__ = [ "Mobile" ]
