from src.models import General, ProjectType
from beanie import Document
from typing import List, Dict, Set, Optional
from bson import ObjectId

class TemplateHandler:
    @staticmethod
    async def get_all_tags() -> Set[str]:
        """Fetch all unique tags from all templates."""
        templates = await TemplateHandler.get_all_templates()

        all_tags = set()
        for template in templates:
            all_tags.update(template["tags"])

        return all_tags

    @staticmethod
    async def get_all_templates(
            project_type: Optional[ProjectType] = None,
            tags: Optional[Set[str]] = None
        ) -> List[Dict]:
        """Fetch all templates based on project type and tags"""
        
        templates = []
        templates.extend(await TemplateHandler._fetch_templates(General))
        if project_type:
            templates = [t for t in templates if t["project_type"] == project_type.value]

        if tags:
            tags_lower = {tag.lower() for tag in tags}
            templates = [
                t for t in templates if any(tag.lower() in tags_lower for tag in t["tags"])
            ]

        return templates

    @staticmethod
    async def get_template_by_id(template_id: str) -> Document | None:
        template = await General.get(template_id)
        if template:
            return template

        return None


    # Private functions 
    async def _fetch_templates(model: General) -> List[Dict]:
        templates = await model.all().to_list()
        return [ await TemplateHandler._format_template(template) for template in templates ]

    async def _format_template(template) -> Dict:
        return {
            "id": str(template.id),
            "name": template.projectName,
            "description": template.projectPlan,
            "project_type": template.projectType.value,
            "tags": set(template.projectTags),
            "file_id": template.projectFileId
        }


__all__ = [ "Templatehandler", "ProjectType"]
