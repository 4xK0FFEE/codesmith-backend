from src.models.pydantic import General
from src.models import ProjectType
from pydantic import Field

class DevOps(General):
    projectType: ProjectType = Field(default=ProjectType.DevOps)
    backup: bool
    cicd: str
    cloudProvider: str
    compliance: bool
    containerization: str
    infrastructure: str
    monitoring: str
    orchestration: str
    security: str
    serviceDiscovery: str

__all__ = [ "DevOps" ]

