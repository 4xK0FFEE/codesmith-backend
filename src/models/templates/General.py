from beanie import Document
from pydantic import BaseModel
from enum import Enum
from typing import List
from bson import ObjectId

class ProjectType(str, Enum):
    Frontend = "frontend"
    Backend = "backend"
    FullStack = "fullstack"
    CLI = "cli"
    Mobile = "mobile"
    AiMl = "ai_ml"
    GameDev = "gamedev"
    DevOps = "devops"
    General = "general"

class General(Document):
    id: str
    projectName: str
    projectAuthor: str
    projectAudience: str
    projectPlan: str
    projectTags: List[str]
    projectType: ProjectType
    projectFileId: int

    class Settings:
        collection = "general_projects"

__all__ = [ "General", "ProjectType" ]
