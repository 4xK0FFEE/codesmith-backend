from src.models.pydantic import General
from src.models import ProjectType
from pydantic import Field

class FullStack(General):
    projectType: ProjectType = Field(default=ProjectType.FullStack)
    authentication: str
    backendFramework: str
    database: str
    deployment: str
    frontendFramework: str
    orm: str

__all__ = [ "FullStack" ]
