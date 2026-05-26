from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from chat_service.router import chat_router

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)
routers = [chat_router]
for router in routers:
    app.include_router(router)
