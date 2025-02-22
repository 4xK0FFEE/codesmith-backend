from beanie import Document
from bson import ObjectId
from typing import List

class Template(Document):
    name: str
    filepath: str
    type: List[str] # FOr now .. later we need to add literal
    stack: List[str]

    class Settings:
        collection = "templates"
