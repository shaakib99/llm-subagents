from langchain.tools import tool
from llm_service.models import AgentResponse
from llm_service.service import LLMService
from llm_service.tools.search_tool import search
from llm_service.service import LLMService

@tool('research_agent', description='A research agent that can perform research tasks and return summaries.')
async def research_agent(query: str) -> AgentResponse:
    '''This agent performs research based on the provided query and returns a summary of the findings.'''
    prompt = f"Do research for this user's query: {query}"
    llm_service = LLMService()
    result = await llm_service.generate_response(prompt=prompt)
    return AgentResponse(result=result)