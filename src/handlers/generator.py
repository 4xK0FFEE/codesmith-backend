from typing import Dict
import os
import json
import re
import shutil
from pathlib import Path
import src.models.pydantic as pydantic_models
from src.models import ProjectType, General
from pydantic import BaseModel
import requests

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
        specific_prompt = ""

        match input_model.projectType:
            case ProjectType.Frontend:
                specific_prompt=f"""The frontend is built using {input_model.framework}. The primary language is {input_model.language}, with {input_model.styling} as the styling solution. State management will be handled using {input_model.stateManagement}, and form handling is done via {input_model.formHandling}. There {"will" if input_model.authentication else "will not"} be Authentication Setup. The project will use {input_model.routing} for routing, {input_model.uiLibrary} for UI components, and {input_model.packageManager} as the package manager. Testing will be handled using {input_model.testing}. Analytics provider is {input_model.analytics}, SEO setup will {"be" if input_model.seo else "will not be"} there, and i18n (Internationalization) setup will {"be" if input_model.i18n else "will not be"}  there. PWA configuration will {"be" if input_model.pwa else "will not be"} there."""
            case ProjectType.Backend:
                specific_prompt = f"""The backend project will be built using {input_model.framework} with {input_model.language} as the primary language.
        API specifications follow {input_model.apiSpec}, and authentication is handled via {input_model.authentication}.
        The database used is {input_model.database}, with {input_model.orm} as the ORM.
        Caching mechanism is {input_model.caching}.
        Containerization is {"enabled" if input_model.docker else "not enabled"}, and messaging service is {input_model.messaging}.
        Monitoring setup is {input_model.monitoring}. Testing will be done using {input_model.testing}."""

            case ProjectType.DevOps:
                specific_prompt = f"""The DevOps project uses {input_model.cloudProvider} as the cloud provider.
        CI/CD is managed through {input_model.cicd}, with {input_model.orchestration} for orchestration and {input_model.infrastructure} for infrastructure management.
        Containerization is handled by {input_model.containerization}, and monitoring is done using {input_model.monitoring}.
        Service discovery is {input_model.serviceDiscovery}, security setup is {input_model.security}.
        {"Include" if input_model.compliance else "Do not include"} compliance and policy as code setup.
        {"Include" if input_model.backup else "Do not include"} backup and disaster recovery setup."""

            case ProjectType.CLI:
                specific_prompt = f"""The CLI project is developed using {input_model.language}.
        It will include {input_model.argumentParser} for argument parsing and {input_model.logging} for logging.
        The CLI {"has" if input_model.interactive else "does not have"} an interactive mode."""

            case ProjectType.AiMl:
                specific_prompt = f"""The AI/ML project focuses on {input_model.projectPlan}.
        It will be developed using {input_model.framework}, with {"GPU support" if input_model.gpuSupport else "no GPU support"}.
        Data processing involves {input_model.dataProcessing}, and experiment tracking is {"enabled" if input_model.experimentTracking else "disabled"}.
        Model tracking is done via {input_model.modelTracking}, and visualization tools include {input_model.visualization}.
        Deployment strategy is {input_model.deployment}."""

            case ProjectType.FullStack:
                specific_prompt = f"""The fullstack project uses {input_model.frontendFramework} for the frontend and {input_model.backendFramework} for the backend.
        The database is {input_model.database}, managed using {input_model.orm}.
        Authentication is set up as {input_model.authentication}.
        The deployment strategy includes {input_model.deployment}."""

            case ProjectType.GameDev:
                specific_prompt = f"""The game development project is a {input_model.dimension} game built using {input_model.engine}.
        The genre is {input_model.genre}, and physics engine is {input_model.physics}.
        Multiplayer support is {"enabled" if input_model.multiplayer else "disabled"},
        {"with" if input_model.assetManagement else "without"} asset management.
        The game {"includes" if input_model.saveSystem else "does not include"} a save system."""

            case ProjectType.Mobile:
                specific_prompt = f"""The mobile project uses {input_model.framework} as the framework.
        State management is handled by {input_model.stateManagement}, and authentication is set up as {input_model.authentication}.
        Navigation solution is {input_model.navigation}, and data storage is managed using {input_model.storage}."""

        prompt = f'''
            My project name is {input_model.projectName}, author is {input_model.projectAuthor} and my audience reach is {input_model.projectAudience}. My project plan is {input_model.projectPlan}.

            {specific_prompt}

            Generate a structured directory layout for this project in the form of a nested list named Structure.

            The output should be a list of tuples where each tuple contains, ensure it is a list:
            1. Level (integer) - Represents the depth of the file/folder in the hierarchy.
            2. Name (string) - The file or folder name.
            3. Type (string) - Either "file" or "folder".
            4. Name for db(string) - this is a string which is a title for a general use of this project so that other people can use it 
            5. Tags(string) - what all tags the project comes under. Like FullStack,Frontend,NextJS,etc.

            Then create boilerplate template code for ALL the files in the directories. Give the output in a dictionary format with the key being the ordered tuple structure you generated for the structure and the value being the boilerplate template code for each respective file as a string with \\n for line breaks.

            Then give a list of scripts in a sequential order as a list of strings.

            And you have to include everything as a list of strings in Python, i.e.

            {{"structure": list of tuples, "scripts": list of strings, "boilerplate": dictionary of ordered tuples and file content}}

            Give only the output i want and no explanation. I need to directly integrate this in my backend. Give the enter keys in the code as \\n.

            This is an example template. Follow the exact same pattern.

            {{
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
                "boilerplate": {{
                    (2, "App.tsx", "file"): "import {{ Button }} from \\"@/components/ui/button\\";\\n\\nfunction App() {{\\n    return (\\n        <div className=\\"flex items-center justify-center h-screen\\">\\n            <Button>Click me</Button>\\n        </div>\\n    );\\n}}\\n\\nexport default App;",

                    (2, "main.tsx", "file"): "import React from \\"react\\";\\nimport ReactDOM from \\"react-dom/client\\";\\nimport App from \\"./App\\";\\nimport \\"./index.css\\";\\n\\nReactDOM.createRoot(document.getElementById(\\"root\\") as HTMLElement).render(\\n    <React.StrictMode>\\n        <App />\\n    </React.StrictMode>\\n);",

                    (2, "manifest.json", "file"): "{{\\n    \\"short_name\\": \\"App\\",\\n    \\"name\\": \\"Project Name\\",\\n    \\"icons\\": [],\\n    \\"start_url\\": \\".\\",\\n    \\"display\\": \\"standalone\\",\\n    \\"theme_color\\": \\"#ffffff\\",\\n    \\"background_color\\": \\"#ffffff\\"\\n}}",

                    (1, "package.json", "file"): "{{\\n    \\"name\\": \\"project-name\\",\\n    \\"version\\": \\"0.1.0\\",\\n    \\"private\\": true,\\n    \\"dependencies\\": {{\\n        \\"react\\": \\"^18.0.0\\",\\n        \\"react-dom\\": \\"^18.0.0\\",\\n        \\"@shadcn/ui\\": \\"latest\\"\\n    }},\\n    \\"devDependencies\\": {{\\n        \\"typescript\\": \\"^5.0.0\\",\\n        \\"vite\\": \\"^4.0.0\\",\\n        \\"tailwindcss\\": \\"latest\\",\\n        \\"postcss\\": \\"latest\\",\\n        \\"autoprefixer\\": \\"latest\\"\\n    }}\\n}}",

                    (1, "tsconfig.json", "file"): "{{\\n    \\"compilerOptions\\": {{\\n        \\"target\\": \\"esnext\\",\\n        \\"module\\": \\"esnext\\",\\n        \\"jsx\\": \\"react-jsx\\",\\n        \\"strict\\": true\\n    }}\\n}}",

                    (1, "tailwind.config.ts", "file"): "import type {{ Config }} from 'tailwindcss';\\n\\nconst config: Config = {{\\n    content: [\\"./index.html\\", \\"./src//*.{{ts,tsx}}\\"],\\n    theme: {{\\n        extend: {{}},\\n    }},\\n    plugins: [],\\n}};\\n\\nexport default config;",

                    (1, "postcss.config.ts", "file"): "export default {{\\n    plugins: {{\\n        tailwindcss: {{}},\\n        autoprefixer: {{}},\\n    }},\\n}};",

                    (1, "vite.config.ts", "file"): "import {{ defineConfig }} from \\"vite\\";\\nimport react from \\"@vitejs/plugin-react\\";\\n\\nexport default defineConfig({{\\n    plugins: [react()],\\n}});",

                    (1, "index.html", "file"): "<!DOCTYPE html>\\n<html lang=\\"en\\">\\n<head>\\n    <meta charset=\\"UTF-8\\" />\\n    <meta name=\\"viewport\\" content=\\"width=device-width, initial-scale=1.0\\" />\\n    <link rel=\\"manifest\\" href=\\"/manifest.json\\" />\\n    <title>Project Name</title>\\n</head>\\n<body>\\n    <div id=\\"root\\"></div>\\n    <script type=\\"module\\" src=\\"/src/main.tsx\\"></script>\\n</body>\\n</html>"
                }},
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
                "name": "Name for db"
            }}'''
        payload = {
            "model": "deepseek-coder:6.7b",
            "prompt": specific_prompt,
            "stream": False
        }
        resp = requests.post("http://localhost:11434/api/generate",)
        ai_response = resp.json()["response"]
        return ai_response

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
