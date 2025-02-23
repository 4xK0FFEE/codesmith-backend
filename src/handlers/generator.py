from typing import Dict
import os
import json
import re
import shutil
from pathlib import Path
import src.models.pydantic as pydantic_models
from src.models import ProjectType
from pydantic import BaseModel

def get_next_zip_number(directory: str = "/files") -> str:
    zip_files = [f for f in os.listdir(directory) if f.endswith(".zip")]
    numbers = []
    for file in zip_files:
        match = re.match(r"(\d+)\.zip$", file)
        if match:
            numbers.append(int(match.group(1)))
    next_number = max(numbers) + 1 if numbers else 1  # Start from 1 if no files exist
    return os.path.join(directory, f"{next_number}.zip")

class GeneratorHandler:
    @staticmethod
    async def generate_file(input_model) -> str:
        #ai_response:str = GeneratorHandler._call_ai(input_model)
        #file_dir:str = await GeneratorHandler._make_file(ai_response)
        #ret_path:str = await GeneratorHandler._make_zip(file_dir)
        #match = re.match(r"(\d+)\.zip$", ret_path)
        #await GeneratorHandler._add_to_db(input_model,match.group(1))
        return f"/file/get/{1}"

    @staticmethod
    async def _add_to_db(input_model:BaseModel, file_id:str)


    @staticmethod
    async def _call_ai(input_model) -> str:
        return 'ai response'

    @staticmethod
    async def _parse_string(input: str) -> Dict:
        return json.loads(input)

    @staticmethod
    async def _make_file(input_str: str) -> str:
        input_dict = GeneratorHandler._parse_string(input_str)
        BASE_PATH = Path("/tmp")
        for i in input_dict["structure"]:
            path = BASE_PATH / i[1]
            if i[2] == "folder":
                path.mkdir(parents=True, exist_ok=True)
            elif i[2] == "file":
                path.touch(exist_ok=True)
        for k,v in input_dict["boilerplate"].items():
            path = BASE_PATH / 
            with open(path,"a") as file:
                file.write(v)
        root_dir = Path(BASE_PATH, i["structure"][0][1])
        for i in input_dict["scripts"]:
            file = "scripts.txt"
            path = root_dir / file
            with open(path,"a") as file:
                file.write(i)
                file.write("\n")
        return root_dir

    @staticmethod
    async def _make_zip(file_path:str) -> str:
        file_name = get_next_zip_number() 
        op_zip = Path("/files",file_name)
        shutil.make_archive(op_zip,'zip',file_name)
        return op_zip
