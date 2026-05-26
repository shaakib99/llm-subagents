from langchain.messages import SystemMessage
from langchain.agents import  AgentMiddleware
from langchain.agents.structured_output import ProviderStrategy
from pydantic import BaseModel, SecretStr
from langchain.tools import BaseTool, tool


class LLMConfig(BaseModel):
    model_name: str
    api_key: SecretStr


class Agent(BaseModel):
    name: str
    description: str
    tool: BaseTool

class AgentResponse(BaseModel):
    result: str

class BaseContext(BaseModel):
    pass

class BaseMetadata(BaseModel):
    tools: list[BaseTool] = []
    middlewares: list[AgentMiddleware] = []
    provider_strategy: ProviderStrategy | None = None
    checkpointer_id: str | None = None
    context: BaseContext | None = None
    system_prompt: SystemMessage | None = None