from beanie import Document,PydanticObjectId
from pydantic import BaseModel
from enum import Enum
from typing import List,Optional
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
    _id: Optional[PydanticObjectId] = None 
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
