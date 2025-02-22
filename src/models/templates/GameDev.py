from src.models.templates.General import General

class GameDev(General):
    assetManagement: bool
    dimension: str
    engine: str
    genre: str
    multiplayer: bool
    physics: str
    saveSystem: bool

    class Settings:
        collection = "gamedev_projects"

__all__ = [ "GameDev" ]
