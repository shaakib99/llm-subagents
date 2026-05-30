from llm_service.models import BaseContext
from llm_service.service import LLMService
from llm_service.models import BaseMetadata
from agents.agent_util import list_agents, call_sub_agent

class ChatService:
    def __init__(self, llm_service = None):
        self.llm = llm_service or LLMService()
    
    async def get_response(self, query:str, metadata: BaseMetadata) -> str:
        metadata = BaseMetadata()
        metadata.context = BaseContext()
        metadata.tools = [list_agents, call_sub_agent]
        metadata.middlewares = []
        metadata.provider_strategy = None
        metadata.checkpointer_id = None
        metadata.system_prompt = 'You are a helpful assistant that can call various agents to assist with user queries. Use the tools provided to call the appropriate agent based on the user query. Always provide a helpful and concise response to the user query after calling the necessary agents. You must ONLY use the provided tools. Do not invent new tools or parameters. If a subagent is not available in the tool definitions, handle the task internally.'
        response = await self.llm.generate_response(query, metadata)
        return response