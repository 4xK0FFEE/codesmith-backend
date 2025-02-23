from pydantic import BaseModel
from src.models import ProjectType
from typing import List

class General(BaseModel):
    projectName: str
    projectAuthor: str
    projectAudience: str
    projectPlan: str
    projectTags: List[str]
    projectType: ProjectType

__all__ = [ "General" ]
