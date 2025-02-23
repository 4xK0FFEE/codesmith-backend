from src.models.pydantic import General
from src.models import ProjectType
from pydantic import Field

class Frontend(General):
    projectType: ProjectType = Field(default=ProjectType.Frontend)
    analytics: str
    authentication: bool
    formHandling: str
    framework: str
    language: str
    packageManager: str
    routing: str
    seo: bool
    stateManagement: str
    styling: str
    testing: str
    uiLibrary: str
    pwa: bool
    i18n: bool

__all__ = [ "Frontend" ]
