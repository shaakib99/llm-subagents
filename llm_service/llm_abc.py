from abc import ABC, abstractmethod
from multiprocessing.context import BaseContext
from typing import AsyncGenerator
from langchain.agents.middleware import AgentMiddleware
from langchain_core.messages import SystemMessage
from langchain.tools import BaseTool
from langchain.agents.structured_output import ProviderStrategy

class LLMABC(ABC):
    @abstractmethod
    async def  generate_response(self, 
                                prompt: str, 
                                name, 
                                context: BaseContext | None, 
                                tools: list[BaseTool], 
                                middlewares: list[AgentMiddleware],
                                provider_strategy: ProviderStrategy,
                                checkpointer_id: str | None = None,
                                system_prompt: SystemMessage = SystemMessage(content="You are a helpful assistant.")) -> str:
        pass

    @abstractmethod
    async def generate_streaming_response(self, 
                                        prompt: str, 
                                        name, 
                                        context: BaseContext | None, 
                                        tools: list[BaseTool], 
                                        middlewares: list[AgentMiddleware],
                                        provider_strategy: ProviderStrategy,
                                        checkpointer_id: str | None = None,
                                        system_prompt: SystemMessage = SystemMessage(content="You are a helpful assistant.")) -> AsyncGenerator[str, None]:
        pass
    