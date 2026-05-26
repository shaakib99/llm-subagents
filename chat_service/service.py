from llm_service.models import BaseContext
from llm_service.service import LLMService
from llm_service.models import BaseMetadata
from agents.agent_util import get_agent, list_agents

class ChatService:
    def __init__(self, llm_service = None):
        self.llm = llm_service or LLMService()
    
    async def get_response(self, query:str, metadata: BaseMetadata) -> str:
        metadata = BaseMetadata()
        metadata.context = BaseContext()
        metadata.tools = [get_agent, list_agents]
        metadata.middlewares = []
        metadata.provider_strategy = None
        metadata.checkpointer_id = None
        metadata.system_prompt = None
        response = await self.llm.generate_response(query, metadata)
        return response