from src.models.pydantic import General

class CLI(General):
    argumentParser: str
    interactive: bool
    language: str
    logging: str

__all__ = [ "CLI" ]
