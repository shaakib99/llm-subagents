from langchain.tools import tool
from llm_service.models import AgentResponse, BaseMetadata
from llm_service.service import LLMService
from llm_service.tools import visit_website, search
from llm_service.service import LLMService

@tool('research_agent', description='A research agent that can perform research tasks and return summaries.')
async def research_agent(query: str) -> AgentResponse:
    '''This agent performs research based on the provided query and returns a summary of the findings.'''
    prompt = f"Do research for this user's query: {query}"
    llm_service = LLMService()
    data = BaseMetadata()
    data.tools = [visit_website, search]
    data.middlewares = []
    result = await llm_service.generate_response(prompt=prompt, data=data)
    return AgentResponse(result=result)