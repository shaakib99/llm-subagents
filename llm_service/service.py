
from llm_service.llm_abc import LLMABC
from llm_service.models import LLMConfig
from llm_service.openrouter_llm import OpenRouterLLM
from typing import AsyncGenerator
from llm_service.models import BaseContext
from agents.agent_util import get_agent, list_agents
import os

class LLMService:
    def __init__(self, llm: LLMABC):
        model_name = os.getenv('LLM_MODEL_NAME', 'gpt-4o')
        api_key = os.getenv('LLM_API_KEY', '')
        self.llm = llm or OpenRouterLLM(LLMConfig(model_name=model_name, api_key=api_key))
    
    async def generate_response(self, prompt: str, data: dict) -> str:
        context = BaseContext()
        tools = data.get('tools', [])
        middlewares = data.get('middlewares', [])
        provider_strategy = data.get('provider_strategy', None)
        checkpointer_id = data.get('checkpointer_id', None)
        system_prompt = data.get('system_prompt', None)

        tools.extend([get_agent, list_agents])
        return await self.llm.generate_response(prompt, context=context, tools=tools, middlewares=middlewares, provider_strategy=provider_strategy, checkpointer_id=checkpointer_id, system_prompt=system_prompt)
    
    async def generate_streaming_response(self, prompt: str, data: dict) -> AsyncGenerator[str, None]:
        context = BaseContext()
        tools = data.get('tools', [])
        middlewares = data.get('middlewares', [])
        provider_strategy = data.get('provider_strategy', None)
        checkpointer_id = data.get('checkpointer_id', None)
        system_prompt = data.get('system_prompt', None)

        tools.extend([get_agent, list_agents])
        async for response in self.llm.generate_streaming_response(prompt, context=context, tools=tools, middlewares=middlewares, provider_strategy=provider_strategy, checkpointer_id=checkpointer_id, system_prompt=system_prompt):
            yield response
        