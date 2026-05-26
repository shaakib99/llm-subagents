from langchain.messages import SystemMessage
from langchain.agents.middleware import AgentMiddleware
from langchain.agents.structured_output import ProviderStrategy
from pydantic import BaseModel, SecretStr
from langchain.tools import BaseTool, tool


class LLMConfig(BaseModel):
    model_name: str
    api_key: SecretStr

class AgentResponse(BaseModel):
    result: str

class Agent(BaseModel):
    name: str
    description: str
    tool: BaseTool

class BaseContext(BaseModel):
    context: str = "" 

class BaseMetadata(BaseModel):
    tools: list[BaseTool] = []
    middlewares: list[AgentMiddleware] = []
    provider_strategy: ProviderStrategy | None = None
    checkpointer_id: str | None = None
    context: BaseContext | None = None
    system_prompt: SystemMessage | None = None

    class Config:
        arbitrary_types_allowed = True