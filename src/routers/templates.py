from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from typing import List, Optional, Set
from src.handlers import TemplateHandler
from src.models import ProjectType
from pydantic import BaseModel

class Template(BaseModel):
    id: str
    name: str
    description: str
    project_type: ProjectType
    tags: Set[str]

class TemplateDownload(Template):
    download_url: str 

router = APIRouter(prefix="/templates", tags=["Template Router"])


@router.get("/all", response_model=List[Template])
async def list_templates(
    project_type: Optional[ProjectType] = None,
    tags: Optional[str] = Query(None, description="Comma-separated list of tags to filter by")
):
    tag_set = set(tags.split(",")) if tags else None
    templates = await TemplateHandler.get_all_templates(project_type, tag_set)
    return [Template(**t) for t in templates]

@router.get("/tags")
async def get_all_tags() -> JSONResponse:
    return JSONResponse({"tags": sorted(list(await TemplateHandler.get_all_tags()))})

@router.get("/{template_id}", response_model=TemplateDownload)
async def get_template(template_id: str):

    template = await TemplateHandler.get_template_by_id(template_id)
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    template["download_url"] = f"/files/download/{template['projectFileId']}"
    template_ret = TemplateDownload(**template)
    return template_ret

__all__ = [ "router" ]
