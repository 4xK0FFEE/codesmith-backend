from src.models.pydantic import General

class Frontend(General):
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
