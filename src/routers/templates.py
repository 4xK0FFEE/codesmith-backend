from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional, Set
from src.handlers.templates import TemplateHandler
from src.models.templates import Template, TemplateList, TemplateCreate, ProjectType

router = APIRouter(prefix="/templates", tags=["Template Router"])
template_handler = TemplateHandler()

@router.get("/all", response_model=List[TemplateList])
async def list_templates(
    project_type: Optional[ProjectType] = None,
    tags: Optional[str] = Query(None, description="Comma-separated list of tags to filter by")
):
    """
    Get all templates with optional filtering by project type and tags.
    Returns a list of templates with basic information (id, name, description, project_type, tags).
    """
    tag_set = set(tags.split(",")) if tags else None
    return template_handler.get_all_templates(project_type, tag_set)

@router.get("/tags")
async def get_all_tags():
    """
    Get all available tags across all templates.
    """
    return {"tags": sorted(list(template_handler.get_all_tags()))}

@router.get("/{template_id}", response_model=Template)
async def get_template(template_id: int):
    """
    Get a specific template by ID.
    Returns complete template information including the download URL and tags.
    """
    template = template_handler.get_template_by_id(template_id)
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    return template

@router.post("/add", response_model=Template)
async def add_template(template: TemplateCreate):
    """
    Add a new template to the system.
    """
    new_template = Template(
        id=0,  # Will be set by the handler
        **template.dict()
    )
    return template_handler.add_template(new_template)

@router.get("/types")
async def get_project_types():
    """
    Get all available project types.
    """
    return [{"name": t.name, "value": t.value} for t in ProjectType]
