from src.models.pydantic import General
from src.models import ProjectType
from pydantic import Field

class AiMl(General):
    projectType: ProjectType = Field(default=ProjectType.AiMl)
    dataProcessing: str
    deployment: str
    experimentTracking: bool
    framework: str
    gpuSupport: bool
    modelTracking: str
    visualization: str

__all__ = [ "AiMl" ]
