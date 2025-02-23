from src.models.pydantic import General

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

__all__ = [ "Backend" ]
