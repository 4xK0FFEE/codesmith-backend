from src.models.pydantic import General

class AiMl(General):
    dataProcessing: str
    deployment: str
    experimentTracking: bool
    framework: str
    gpuSupport: bool
    modelTracking: str
    visualization: str

__all__ = [ "AiMl" ]
