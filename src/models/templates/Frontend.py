from src.models.templates.General import General

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

    class Settings:
        collection = "frontend_projects"

__all__ = [ "Frontend" ]
