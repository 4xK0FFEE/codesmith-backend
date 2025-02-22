from src.models.templates.General import General

class Backend(General):
    apiSpec: str
    authentication: str
    caching: str
    database: str
    docker: bool
    framework: str
    language: str
    messaging: str
    monitoring: str
    orm: str
    testing: str

    class Settings:
        collection = "backend_projects"

__all__ = [ "Backend" ]
