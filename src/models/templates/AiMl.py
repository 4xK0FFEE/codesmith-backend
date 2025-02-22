from src.models.templates.General import General

class AiMl(General):
    dataProcessing: str
    deployment: str
    experimentTracking: bool
    framework: str
    gpuSupport: bool
    modelTracking: str
    visualization: str

    class Settings:
        collection = "ai_ml_projects"

__all__ = [ "AiMl" ]
