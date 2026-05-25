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