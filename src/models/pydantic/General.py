from pydantic import BaseModel
from src.models import ProjectType

class General(BaseModel):
    id: str
    projectName: str
    projectAuthor: str
    projectAudience: str
    projectPlan: str
    projectTags: List[str]
    projectType: ProjectType
    projectFileId: int

__all__ = [ "General" ]
