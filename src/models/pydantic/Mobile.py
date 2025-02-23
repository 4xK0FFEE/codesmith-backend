from src.models.pydantic import General
from src.models import ProjectType
from pydantic import Field

class Mobile(General):
    projectType: ProjectType = Field(default=ProjectType.Mobile)
    authentication: str
    framework: str
    navigation: str
    stateManagement: str
    storage: str

__all__ = [ "Mobile" ]
