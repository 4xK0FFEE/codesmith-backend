from fastapi import APIRouter, Response

router = APIRouter(tags=["Generator"])

@router.post("/frontend", tags = ["Generator"])
async def generator_frontend():
    return Response('frontend')

@router.post("/backend", tags = ["Generator"])
async def generator_backend():
    return Response("backend")

@router.post("/fullstack", tags = ["Generator"])
async def generator_backend():
    return Response("fullstack")

@router.post("/cli", tags = ["Generator"])
async def generator_cli():
    return Response("cli")

@router.post("/mobile", tags = ["Generator"])
async def generator_mobile():
    return Response("mobile")

@router.post("/ai-ml", tags = ["Generator"])
async def generator_ai_ml():
    return Response("ai-ml")

@router.post("/game-dev", tags = ["Generator"])
async def generator_game():
    return Response("game dev")

@router.post("/devops", tags = ["Generator"])
async def generator_devops():
    return Response("devops")
