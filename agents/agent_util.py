from langchain.tools import BaseTool, tool
from agents import research_agent
from llm_service.models import Agent
from typing import Dict, Any

agents_list: list[Agent] = [
    Agent(
        name="Research Agent",
        description='''An agent that can perform research tasks and return summaries. 
        "Parameters: query (str): The research query provided by the user.''',
        tool=research_agent
    ),
]

@tool("call_sub_agent", description="You can call a specific agent listed in list_agents tool with required parameter in arguments.")
async def call_sub_agent(agent_name: str, arguments: Dict[str, Any] = {}) -> str:
    '''
    Args: 
    agent_name (str): The name of the agent to call.
    arguments (Dict[str, Any]): The parameters required by the specific sub agent being called in dict format.

    Example:
    If you want to call the Research Agent with a query parameter, your input would look like this:
    {
        "agent_name": "Research Agent",
        "arguments": {
            "query": "What is the capital of France?"
        }
    }
    This tool allows you to call a specific agent listed in list_agents by its name and pass the necessary parameters for that agent in the arguments parameter.'''
    agent = next((agent for agent in agents_list if agent.name == agent_name), None)
    if not agent:
        return f"Agent '{agent_name}' not found."
    return await agent.tool.arun(tool_input=arguments)

@tool("list_agents", description="List all available agents and tools.")
def list_agents() -> list[dict[str, str]]:
    return [{"agent_name": agent.name, "description": agent.description} for agent in agents_list]