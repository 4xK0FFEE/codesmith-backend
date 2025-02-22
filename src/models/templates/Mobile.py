from src.models.templates.General import General

class Mobile(General):
    authentication: str
    framework: str
    navigation: str
    stateManagement: str
    storage: str

    class Settings:
        collection = "mobile_projects"

__all__ = [ "Mobile" ]
