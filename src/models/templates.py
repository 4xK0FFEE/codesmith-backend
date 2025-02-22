from enum import Enum
from pydantic import BaseModel
from typing import Optional, Set

class ProjectType(str, Enum):
    FRONTEND = "frontend"
    BACKEND = "backend"
    FULLSTACK = "fullstack"
    CLI = "cli"
    MOBILE = "mobile"
    AI_ML = "ai-ml"
    GAME_DEV = "game-dev"
    DEVOPS = "devops"

class TemplateBase(BaseModel):
    name: str
    description: str
    project_type: ProjectType
    tags: Set[str]  # Using Set to ensure unique tags

class TemplateCreate(TemplateBase):
    download_url: str

class Template(TemplateBase):
    id: int
    download_url: str

class TemplateList(BaseModel):
    id: int
    name: str
    description: str
    project_type: ProjectType
    tags: Set[str]
