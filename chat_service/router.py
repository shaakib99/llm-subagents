from fastapi import APIRouter
from chat_service.service import ChatService
from llm_service.models import BaseMetadata

chat_router = APIRouter(prefix="/chat", tags=["Chat"])

chat_service = ChatService()

@chat_router.get("/ping")
async def ping():
    return {"message": "pong"}

@chat_router.post("/generate")
async def generate_response(data: dict):
    prompt = data.get("prompt", "")
    return await chat_service.get_response(prompt, BaseMetadata())