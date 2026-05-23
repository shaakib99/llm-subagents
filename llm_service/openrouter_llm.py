from llm_service.llm_abc import LLMABC
from llm_service.models import LLMConfig
from langchain.agents import create_agent
from langchain_openrouter import ChatOpenRouter
from typing import AsyncGenerator

class OpenRouterLLM(LLMABC):
    def __init__(self, llm_config: LLMConfig):
        self.model = ChatOpenRouter(name=llm_config.model_name, api_key=llm_config.api_key)
    
    async def generate_response(self, prompt: str) -> AsyncGenerator[str, None]:
        pass