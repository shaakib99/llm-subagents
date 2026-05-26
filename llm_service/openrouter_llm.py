from llm_service.llm_abc import LLMABC
from llm_service.models import LLMConfig, BaseContext, AgentResponse
from langchain.agents import create_agent
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langchain.agents.middleware import AgentMiddleware
from langchain_core.runnables import Runnable
from langchain.agents.structured_output import ProviderStrategy
from langchain_openrouter import ChatOpenRouter
from typing import AsyncGenerator
from langchain.tools import BaseTool
from langgraph.checkpoint.memory import InMemorySaver

class OpenRouterLLM(LLMABC):
    def __init__(self, llm_config: LLMConfig):
        self.model = ChatOpenRouter(model=llm_config.model_name, api_key=llm_config.api_key)
    
    def __create_agent(self, 
                       name: str, 
                       model: ChatOpenRouter, 
                       tools: list[BaseTool], context: 
                       BaseContext, middlewares: list[AgentMiddleware],
                       provider_strategy: ProviderStrategy,
                       checkpointer_id: str | None,
                       system_prompt: SystemMessage) -> Runnable:
        return create_agent(
            name=name,
            llm=model,
            system_message=system_prompt,
            tools=tools,
            verbose=True,
            middlewares=middlewares,
            context_schema=BaseContext,
            context=context,
            checkpointer_id=checkpointer_id,
            provider_strategy=provider_strategy,
            checkpointer = InMemorySaver() if checkpointer_id else None
        )

    async def generate_response(self, 
                                query: str, 
                                name='', 
                                context: BaseContext | None = None, 
                                tools: list[BaseTool] = [], 
                                middlewares: list[AgentMiddleware] = [],
                                provider_strategy: ProviderStrategy = ProviderStrategy(AgentResponse),
                                checkpointer_id: str | None = None,
                                system_prompt: SystemMessage = SystemMessage(content="You are a helpful assistant.")) -> str:
        
        agent = self.__create_agent(name, self.model, tools, context, middlewares, provider_strategy, checkpointer_id, system_prompt)
        
        result = await agent.ainvoke({'messages': [HumanMessage(content=query)]}, config={}, version='v2')
        return result.content
    
    async def generate_streaming_response(self, 
                                query: str, 
                                name='', 
                                context: BaseContext | None = None, 
                                tools: list[BaseTool] = [], 
                                middlewares: list[AgentMiddleware] = [],
                                provider_strategy: ProviderStrategy = ProviderStrategy(AgentResponse),
                                checkpointer_id: str | None = None,
                                system_prompt: SystemMessage = SystemMessage(content="You are a helpful assistant.")) -> AsyncGenerator[str, None]:
        
        agent = self.__create_agent(name, self.model, tools, context, middlewares, provider_strategy, checkpointer_id, system_prompt)
        
        async for message in agent.astream({'messages': [HumanMessage(content=query)]}, config={}, stream_mode='messages', version='v2'):
            if isinstance(message, AIMessage):
                yield message.content