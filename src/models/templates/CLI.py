from src.models.templates.General import General

class CLI(General):
    argumentParser: str
    interactive: bool
    language: str
    logging: str

    class Settings:
        collection = "cli_projects"

__all__ = [ "CLI" ]
