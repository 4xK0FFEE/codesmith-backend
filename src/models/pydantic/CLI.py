from src.models.pydantic import General
from src.models import ProjectType
from pydantic import Field

class CLI(General):
    projectType:ProjectType = Field(default=ProjectType.CLI)
    argumentParser: str
    interactive: bool
    language: str
    logging: str

__all__ = [ "CLI" ]
