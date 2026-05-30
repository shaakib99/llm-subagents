import asyncio
import sys
from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from chat_service.router import chat_router

load_dotenv()
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)
routers = [chat_router]
for router in routers:
    app.include_router(router)
