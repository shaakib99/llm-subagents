from fastapi import APIRouter

chat_router = APIRouter(prefix="/chat", tags=["Chat"])

@chat_router.get("/ping")
async def ping():
    return {"message": "pong"}

@chat_router.post("/generate")
async def generate_response(prompt: str):
    # Here you would call your LLMService to generate a response based on the prompt
    # For now, we'll just return a dummy response
    return {"response": f"Generated response for prompt: {prompt}"}