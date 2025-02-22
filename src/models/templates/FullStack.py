from src.models.templates.General import General

class FullStack(General):
    authentication: str
    backendFramework: str
    database: str
    deployment: str
    frontendFramework: str
    orm: str

    class Settings:
        collection = "fullstack_projects"

__all__ = [ "FullStack" ]
