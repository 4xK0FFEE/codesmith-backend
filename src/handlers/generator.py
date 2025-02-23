from typing import Dict
import os
import json
from pathlib import Path
import src.models.pydantic as pydantic_models
from src.models import ProjectType

class GeneratorHandler:
    @staticmethod
    async def generate_file(input_model) -> str:
        await GeneratorHandler._parse_string(input)
        return '1'

    @staticmethod
    async def _parse_string(input: str) -> Dict:
        await GeneratorHandler._make_file(json.loads(input))
        return json.loads(input)

    @staticmethod
    async def _make_file(input: Dict):
        BASE_PATH = Path("/tmp")
        for i in input["structure"]:
            path = BASE_PATH / i[1]
            if i[2] == "folder":
                path.mkdir(parents=True, exist_ok=True)
            elif i[2] == "file":
                path.touch(exist_ok=True)
        for k,v in input["boilerplate"].items():
            path = BASE_PATH / k
            with open(path,"a") as file:
                file.write(v)
        root_dir = Path(BASE_PATH, i["structure"][0][1])
        for i in input["scripts"]:
            file = "scripts.txt"
            path = root_dir / file
            with open(path,"a") as file:
                file.write(i)
                file.write("\n")

