from pydantic import BaseModel, SecretStr

class Agent(BaseModel):
    name: str
    description: str

class LLMConfig(BaseModel):
    model_name: str
    api_key: SecretStr