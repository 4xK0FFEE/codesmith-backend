from beanie import Document
from pydantic import BaseModel
from enum import Enum
from typing import List

class ProjectType(str, Enum):
    frontend = "frontend"
    backend = "backend"
    fullstack = "fullstack"
    cli = "cli"
    mobile = "mobile"
    ai_ml = "ai_ml"
    gamedev = "gamedev"
    devops = "devops"

class General(Document):
    projectName: str
    projectAuthor: str
    projectAudience: str
    projectPlan: str
    projectTags: List[str]
    projectType: ProjectType

    class Settings:
        collection = "general_projects"

__all__ = [ "General", "ProjectType" ]
