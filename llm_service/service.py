
from llm_service.llm_abc import LLMABC
from llm_service.models import LLMConfig
from llm_service.openrouter_llm import OpenRouterLLM
from typing import AsyncGenerator
from llm_service.models import BaseContext
from llm_service.models import BaseMetadata
import os

class LLMService:
    def __init__(self, llm: LLMABC | None = None):
        self.llm = llm or OpenRouterLLM(LLMConfig(model_name=os.getenv('OPENROUTER_MODEL_NAME', 'gpt-3.5-turbo'), api_key=os.getenv('OPENROUTER_API_KEY', 'test')))
    
    async def generate_response(self, prompt: str, data: BaseMetadata) -> str:
        context = data.context or BaseContext()
        tools = data.tools or []
        middlewares = data.middlewares or []
        provider_strategy = data.provider_strategy
        checkpointer_id = data.checkpointer_id
        system_prompt = data.system_prompt

        return await self.llm.generate_response(prompt, context=context, tools=tools, middlewares=middlewares, provider_strategy=provider_strategy, checkpointer_id=checkpointer_id, system_prompt=system_prompt)
    
    async def generate_streaming_response(self, prompt: str, data: dict) -> AsyncGenerator[str, None]:
        context = BaseContext()
        tools = data.get('tools', [])
        middlewares = data.get('middlewares', [])
        provider_strategy = data.get('provider_strategy', None)
        checkpointer_id = data.get('checkpointer_id', None)
        system_prompt = data.get('system_prompt', None)

        async for response in self.llm.generate_streaming_response(prompt, context=context, tools=tools, middlewares=middlewares, provider_strategy=provider_strategy, checkpointer_id=checkpointer_id, system_prompt=system_prompt):
            yield response
        