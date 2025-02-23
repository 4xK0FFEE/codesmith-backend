from src.models.pydantic import General
from src.models import ProjectType
from pydantic import Field

class GameDev(General):
    projectType: ProjectType = Field(default=ProjectType.GameDev)
    assetManagement: bool
    dimension: str
    engine: str
    genre: str
    multiplayer: bool
    physics: str
    saveSystem: bool

__all__ = [ "GameDev" ]
