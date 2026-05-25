from langchain.tools import tool
from llm_service.models import AgentResponse
from llm_service.service import LLMService
from llm_service.tools.search_tool import search

@tool('research_agent', description='A research agent that can perform research tasks and return summaries.')
async def research_agent(prompt: str) -> AgentResponse:
    '''This agent performs research based on the provided prompt and returns a summary of the findings.'''
    result = f"Summary of research for: {prompt}"
    return AgentResponse(result=result)