from pydantic import BaseModel, SecretStr

class LLMConfig(BaseModel):
    model_name: str
    api_key: SecretStr