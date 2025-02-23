from src.models.pydantic import General

class GameDev(General):
    assetManagement: bool
    dimension: str
    engine: str
    genre: str
    multiplayer: bool
    physics: str
    saveSystem: bool

__all__ = [ "GameDev" ]
