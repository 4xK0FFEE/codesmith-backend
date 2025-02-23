from src.models.pydantic import General
from src.models import ProjectType
from pydantic import Field

class Backend(General):
    projectType: ProjectType = Field(default=ProjectType.Backend)
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
