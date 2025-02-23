from src.models.templates.General import General

class DevOps(General):
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

    class Settings:
        collection = "devops_projects"

__all__ = [ "DevOps" ]
