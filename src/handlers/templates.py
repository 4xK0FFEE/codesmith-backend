from typing import List, Optional, Set
from src.models.templates import Template, TemplateList, ProjectType

class TemplateHandler:
    def __init__(self):
        # This is a mock database. In production, you should use a proper database
        self.templates = [
            {
                "id": 1,
                "name": "Next.js + FastAPI + PostgreSQL Stack",
                "description": "Modern full-stack template with Next.js frontend, FastAPI backend, and PostgreSQL database with authentication and Docker setup.",
                "project_type": ProjectType.FULLSTACK,
                "download_url": "https://github.com/your-repo/nextjs-fastapi-postgres/archive/main.zip",
                "tags": {"Fullstack", "Next.js", "FastAPI", "PostgreSQL", "Docker", "TypeScript", "Python"}
            },
            {
                "id": 2,
                "name": "MERN Stack + TypeScript + GraphQL",
                "description": "MongoDB, Express.js, React, and Node.js stack with TypeScript and GraphQL integration, including authentication and testing setup.",
                "project_type": ProjectType.FULLSTACK,
                "download_url": "https://github.com/your-repo/mern-typescript-graphql/archive/main.zip",
                "tags": {"Fullstack", "MongoDB", "Express", "React", "Node.js", "TypeScript", "GraphQL"}
            },
            {
                "id": 3,
                "name": "SvelteKit + Supabase + Tailwind",
                "description": "Full-stack SvelteKit application with Supabase backend, Tailwind CSS, and authentication system.",
                "project_type": ProjectType.FULLSTACK,
                "download_url": "https://github.com/your-repo/sveltekit-supabase-tailwind/archive/main.zip",
                "tags": {"Fullstack", "SvelteKit", "Supabase", "Tailwind", "TypeScript"}
            },
            {
                "id": 4,
                "name": "React + Redux Toolkit + RTK Query",
                "description": "Modern React frontend with Redux Toolkit and RTK Query for state management and API calls.",
                "project_type": ProjectType.FRONTEND,
                "download_url": "https://github.com/your-repo/react-rtk-query/archive/main.zip",
                "tags": {"Frontend", "React", "Redux", "RTK Query", "TypeScript"}
            },
            {
                "id": 5,
                "name": "Vue 3 + Pinia + Vue Query",
                "description": "Vue 3 frontend with Pinia state management and Vue Query for data fetching.",
                "project_type": ProjectType.FRONTEND,
                "download_url": "https://github.com/your-repo/vue3-pinia-query/archive/main.zip",
                "tags": {"Frontend", "Vue.js", "Pinia", "Vue Query", "TypeScript"}
            },
            {
                "id": 6,
                "name": "Svelte + TanStack Query + Zustand",
                "description": "Svelte frontend with TanStack Query for data fetching and Zustand for state management.",
                "project_type": ProjectType.FRONTEND,
                "download_url": "https://github.com/your-repo/svelte-query-zustand/archive/main.zip",
                "tags": {"Frontend", "Svelte", "TanStack Query", "Zustand", "TypeScript"}
            },
            {
                "id": 7,
                "name": "FastAPI + SQLModel + Celery",
                "description": "FastAPI backend with SQLModel ORM and Celery for background tasks.",
                "project_type": ProjectType.BACKEND,
                "download_url": "https://github.com/your-repo/fastapi-sqlmodel-celery/archive/main.zip",
                "tags": {"Backend", "FastAPI", "SQLModel", "Celery", "Python"}
            },
            {
                "id": 8,
                "name": "NestJS + TypeORM + Bull Queue",
                "description": "NestJS backend with TypeORM for database operations and Bull for job queues.",
                "project_type": ProjectType.BACKEND,
                "download_url": "https://github.com/your-repo/nestjs-typeorm-bull/archive/main.zip",
                "tags": {"Backend", "NestJS", "TypeORM", "Bull", "TypeScript"}
            },
            {
                "id": 9,
                "name": "Django + DRF + Channels",
                "description": "Django backend with Django REST Framework and Channels for WebSocket support.",
                "project_type": ProjectType.BACKEND,
                "download_url": "https://github.com/your-repo/django-drf-channels/archive/main.zip",
                "tags": {"Backend", "Django", "DRF", "Channels", "Python"}
            },
            {
                "id": 10,
                "name": "React Native + Firebase + MobX",
                "description": "React Native mobile app with Firebase backend and MobX state management.",
                "project_type": ProjectType.MOBILE,
                "download_url": "https://github.com/your-repo/react-native-firebase-mobx/archive/main.zip",
                "tags": {"Mobile", "React Native", "Firebase", "MobX", "TypeScript"}
            },
            {
                "id": 11,
                "name": "Flutter + Supabase + Riverpod",
                "description": "Flutter mobile app with Supabase backend and Riverpod state management.",
                "project_type": ProjectType.MOBILE,
                "download_url": "https://github.com/your-repo/flutter-supabase-riverpod/archive/main.zip",
                "tags": {"Mobile", "Flutter", "Supabase", "Riverpod", "Dart"}
            },
            {
                "id": 12,
                "name": "Ionic + Capacitor + VueX",
                "description": "Ionic mobile app with Capacitor for native features and VueX state management.",
                "project_type": ProjectType.MOBILE,
                "download_url": "https://github.com/your-repo/ionic-capacitor-vuex/archive/main.zip",
                "tags": {"Mobile", "Ionic", "Capacitor", "Vue.js", "TypeScript"}
            },
            {
                "id": 13,
                "name": "FastAPI + PyTorch + MLflow",
                "description": "AI service with FastAPI backend, PyTorch models, and MLflow for experiment tracking.",
                "project_type": ProjectType.AI_ML,
                "download_url": "https://github.com/your-repo/fastapi-pytorch-mlflow/archive/main.zip",
                "tags": {"AI-ML", "FastAPI", "PyTorch", "MLflow", "Python"}
            },
            {
                "id": 14,
                "name": "TensorFlow + Streamlit + MongoDB",
                "description": "Machine learning application with TensorFlow, Streamlit UI, and MongoDB for data storage.",
                "project_type": ProjectType.AI_ML,
                "download_url": "https://github.com/your-repo/tensorflow-streamlit-mongo/archive/main.zip",
                "tags": {"AI-ML", "TensorFlow", "Streamlit", "MongoDB", "Python"}
            },
            {
                "id": 15,
                "name": "Hugging Face + Gradio + PostgreSQL",
                "description": "NLP application with Hugging Face models, Gradio interface, and PostgreSQL database.",
                "project_type": ProjectType.AI_ML,
                "download_url": "https://github.com/your-repo/huggingface-gradio-postgres/archive/main.zip",
                "tags": {"AI-ML", "Hugging Face", "Gradio", "PostgreSQL", "Python"}
            },
            {
                "id": 16,
                "name": "Unity + Mirror + PostgreSQL",
                "description": "Multiplayer game template with Unity engine, Mirror networking, and PostgreSQL database.",
                "project_type": ProjectType.GAME_DEV,
                "download_url": "https://github.com/your-repo/unity-mirror-postgres/archive/main.zip",
                "tags": {"Game-Dev", "Unity", "Mirror", "PostgreSQL", "C#"}
            },
            {
                "id": 17,
                "name": "Godot + Nakama + TypeScript",
                "description": "Multiplayer game template with Godot engine, Nakama server, and TypeScript support.",
                "project_type": ProjectType.GAME_DEV,
                "download_url": "https://github.com/your-repo/godot-nakama-typescript/archive/main.zip",
                "tags": {"Game-Dev", "Godot", "Nakama", "TypeScript"}
            },
            {
                "id": 18,
                "name": "Unreal + PlayFab + PostgreSQL",
                "description": "Online game template with Unreal Engine, PlayFab backend, and PostgreSQL database.",
                "project_type": ProjectType.GAME_DEV,
                "download_url": "https://github.com/your-repo/unreal-playfab-postgres/archive/main.zip",
                "tags": {"Game-Dev", "Unreal Engine", "PlayFab", "PostgreSQL", "C++"}
            },
            {
                "id": 19,
                "name": "Python + Click + Rich",
                "description": "Modern CLI application template with Click for commands and Rich for terminal formatting.",
                "project_type": ProjectType.CLI,
                "download_url": "https://github.com/your-repo/python-click-rich/archive/main.zip",
                "tags": {"CLI", "Python", "Click", "Rich"}
            },
            {
                "id": 20,
                "name": "Rust + Clap + SQLite",
                "description": "High-performance CLI tool with Clap for argument parsing and SQLite for local storage.",
                "project_type": ProjectType.CLI,
                "download_url": "https://github.com/your-repo/rust-clap-sqlite/archive/main.zip",
                "tags": {"CLI", "Rust", "Clap", "SQLite"}
            },
            {
                "id": 21,
                "name": "Go + Cobra + BoltDB",
                "description": "Go CLI application with Cobra framework and BoltDB for embedded database.",
                "project_type": ProjectType.CLI,
                "download_url": "https://github.com/your-repo/go-cobra-boltdb/archive/main.zip",
                "tags": {"CLI", "Go", "Cobra", "BoltDB"}
            },
            {
                "id": 22,
                "name": "Terraform + AWS + GitHub Actions",
                "description": "Infrastructure as Code with Terraform, AWS resources, and GitHub Actions for CI/CD.",
                "project_type": ProjectType.DEVOPS,
                "download_url": "https://github.com/your-repo/terraform-aws-actions/archive/main.zip",
                "tags": {"DevOps", "Terraform", "AWS", "GitHub Actions"}
            },
            {
                "id": 23,
                "name": "Kubernetes + ArgoCD + Prometheus",
                "description": "Kubernetes cluster setup with ArgoCD for GitOps and Prometheus for monitoring.",
                "project_type": ProjectType.DEVOPS,
                "download_url": "https://github.com/your-repo/k8s-argo-prometheus/archive/main.zip",
                "tags": {"DevOps", "Kubernetes", "ArgoCD", "Prometheus"}
            },
            {
                "id": 24,
                "name": "Ansible + Docker + Grafana",
                "description": "Infrastructure automation with Ansible, Docker containers, and Grafana dashboards.",
                "project_type": ProjectType.DEVOPS,
                "download_url": "https://github.com/your-repo/ansible-docker-grafana/archive/main.zip",
                "tags": {"DevOps", "Ansible", "Docker", "Grafana"}
            }
        ];

    def get_all_templates(
        self,
        project_type: Optional[ProjectType] = None,
        tags: Optional[Set[str]] = None
    ) -> List[TemplateList]:
        templates = self.templates

        # Filter by project type if specified
        if project_type:
            templates = [t for t in templates if t["project_type"] == project_type]

        # Filter by tags if specified
        if tags:
            # Convert tags to lowercase for case-insensitive comparison
            tags_lower = {tag.lower() for tag in tags}
            templates = [
                t for t in templates
                if any(tag.lower() in tags_lower for tag in t["tags"])
            ]

        return [TemplateList(**t) for t in templates]

    def get_template_by_id(self, template_id: int) -> Optional[Template]:
        template = next((t for t in self.templates if t["id"] == template_id), None)
        if template:
            return Template(**template)
        return None

    def add_template(self, template: Template) -> Template:
        new_id = max(t["id"] for t in self.templates) + 1
        template_dict = template.dict()
        template_dict["id"] = new_id
        self.templates.append(template_dict)
        return Template(**template_dict)

    def get_all_tags(self) -> Set[str]:
        """Get all unique tags across all templates"""
        all_tags = set()
        for template in self.templates:
            all_tags.update(template["tags"])
        return all_tags
