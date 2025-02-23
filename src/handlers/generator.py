from typing import Dict
import os
import json
import re
import shutil
from pathlib import Path
import src.models.pydantic as pydantic_models
from src.models import ProjectType, General
from pydantic import BaseModel

def get_next_zip_number(directory: str = "/files") -> str:
    zip_files = [f for f in os.listdir(directory) if f.endswith(".zip")]
    numbers = []
    for file in zip_files:
        match = re.match(r"(\d+)\.zip$", file)
        if match:
            numbers.append(int(match.group(1)))
    next_number = max(numbers) + 1 if numbers else 1
    return f"{next_number}"

class GeneratorHandler:
    @staticmethod
    async def generate_file(input_model) -> str:
        ai_response:str = await GeneratorHandler._call_ai(input_model)
        file_dir:str = await GeneratorHandler._make_file(ai_response)
        ret_path:str = await GeneratorHandler._make_zip(file_dir)
        await GeneratorHandler._add_to_db(input_model,ret_path)
        return f"/files/download/{ret_path}"

    @staticmethod
    async def _add_to_db(input_model, file_id:str):
        project =  General(
            projectName = input_model.projectName,
            projectAuthor = input_model.projectAuthor,
            projectAudience = input_model.projectAudience,
            projectPlan = input_model.projectPlan,
            projectTags = input_model.projectTags,
            projectType = input_model.projectType,
            projectFileId = int(file_id)
        )
        await project.insert()


    @staticmethod
    async def _call_ai(input_model) -> str:
        fake_data = '''{
    "structure": [
        [0, "Project Name", "folder"],
        [1, "Project Name/src", "folder"],
        [2, "Project Name/src/components", "folder"],
        [2, "Project Name/src/pages", "folder"],
        [2, "Project Name/src/App.tsx", "file"],
        [2, "Project Name/src/main.tsx", "file"],
        [1, "Project Name/public", "folder"],
        [2, "Project Name/public/manifest.json", "file"],
        [1, "Project Name/package.json", "file"],
        [1, "Project Name/tsconfig.json", "file"],
        [1, "Project Name/tailwind.config.ts", "file"],
        [1, "Project Name/postcss.config.ts", "file"],
        [1, "Project Name/vite.config.ts", "file"],
        [1, "Project Name/index.html", "file"]
    ],
    "boilerplate": {
        "Project Name/src/App.tsx": "import { Button } from \\\"@/components/ui/button\\\";\\n\\nfunction App() {\\n    return (\\n        <div className='flex items-center justify-center h-screen'>\\n            <Button>Click me</Button>\\n        </div>\\n    );\\n}\\n\\nexport default App;",
        "Project Name/src/main.tsx": "import React from \\\"react\\\";\\nimport ReactDOM from \\\"react-dom/client\\\";\\nimport App from \\\"./App\\\";\\nimport \\\"./index.css\\\";\\n\\nReactDOM.createRoot(document.getElementById(\\\"root\\\") as HTMLElement).render(\\n    <React.StrictMode>\\n        <App />\\n    </React.StrictMode>\\n);",
        "Project Name/public/manifest.json": "{\\n    \\\"short_name\\\": \\\"App\\\",\\n    \\\"name\\\": \\\"Project Name\\\",\\n    \\\"icons\\\": [],\\n    \\\"start_url\\\": \\\".\\\",\\n    \\\"display\\\": \\\"standalone\\\",\\n    \\\"theme_color\\\": \\\"#ffffff\\\",\\n    \\\"background_color\\\": \\\"#ffffff\\\"\\n}",
        "Project Name/package.json": "{\\n    \\\"name\\\": \\\"project-name\\\",\\n    \\\"version\\\": \\\"0.1.0\\\",\\n    \\\"private\\\": true,\\n    \\\"dependencies\\\": {\\n        \\\"react\\\": \\\"^18.0.0\\\",\\n        \\\"react-dom\\\": \\\"^18.0.0\\\",\\n        \\\"@shadcn/ui\\\": \\\"latest\\\"\\n    },\\n    \\\"devDependencies\\\": {\\n        \\\"typescript\\\": \\\"^5.0.0\\\",\\n        \\\"vite\\\": \\\"^4.0.0\\\",\\n        \\\"tailwindcss\\\": \\\"latest\\\",\\n        \\\"postcss\\\": \\\"latest\\\",\\n        \\\"autoprefixer\\\": \\\"latest\\\"\\n    }\\n}",
        "Project Name/tsconfig.json": "{\\n    \\\"compilerOptions\\\": {\\n        \\\"target\\\": \\\"esnext\\\",\\n        \\\"module\\\": \\\"esnext\\\",\\n        \\\"jsx\\\": \\\"react-jsx\\\",\\n        \\\"strict\\\": true\\n    }\\n}",
        "Project Name/tailwind.config.ts": "import type { Config } from 'tailwindcss';\\n\\nconst config: Config = {\\n    content: [\\\"./index.html\\\", \\\"./src/*/.{ts,tsx}\\\"],\\n    theme: {\\n        extend: {}\\n    },\\n    plugins: []\\n};\\n\\nexport default config;",
        "Project Name/postcss.config.ts": "export default {\\n    plugins: {\\n        tailwindcss: {},\\n        autoprefixer: {}\\n    }\\n};",
        "Project Name/vite.config.ts": "import { defineConfig } from \\\"vite\\\";\\nimport react from \\\"@vitejs/plugin-react\\\";\\n\\nexport default defineConfig({\\n    plugins: [react()]\\n});",
        "Project Name/index.html": "<!DOCTYPE html>\\n<html lang=\\\"en\\\">\\n<head>\\n    <meta charset=\\\"UTF-8\\\" />\\n    <meta name=\\\"viewport\\\" content=\\\"width=device-width, initial-scale=1.0\\\" />\\n    <link rel=\\\"manifest\\\" href=\\\"/manifest.json\\\" />\\n    <title>Project Name</title>\\n</head>\\n<body>\\n    <div id=\\\"root\\\"></div>\\n    <script type=\\\"module\\\" src=\\\"/src/main.tsx\\\"></script>\\n</body>\\n</html>"
    },
    "scripts": [
        "npm install",
        "npm run dev",
        "npm run build",
        "npm run preview"
    ],
    "tags": [
        "Frontend",
        "Backend"
    ],
    "name": "idktesting"
}'''
        return fake_data

    @staticmethod
    async def _parse_string(input: str) -> Dict:
        return json.loads(input)

    @staticmethod
    async def _make_file(input_str: str) -> str:
        input_dict = await GeneratorHandler._parse_string(input_str)
        BASE_PATH = Path("/tmp")
        for i in input_dict["structure"]:
            path = BASE_PATH / i[1]
            if i[2] == "folder":
                path.mkdir(parents=True, exist_ok=True)
            elif i[2] == "file":
                path.touch(exist_ok=True)
        for k,v in input_dict["boilerplate"].items():
            path = BASE_PATH / k 
            with open(path,"a") as file:
                file.write(v)
        root_dir = Path(BASE_PATH, input_dict["structure"][0][1])
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
        shutil.make_archive(op_zip,'zip',file_path)
        print(op_zip,flush=True)
        return file_name 
