from src.models.pydantic import General

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

__all__ = [ "DevOps" ]

