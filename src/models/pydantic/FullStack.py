from src.models.pydantic import General

class FullStack(General):
    authentication: str
    backendFramework: str
    database: str
    deployment: str
    frontendFramework: str
    orm: str

__all__ = [ "FullStack" ]
