from langchain.tools import BaseTool, tool
from agents import research_agent
from llm_service.models import Agent, SubAgentCallSchema
from typing import Dict, Any

agents_list: list[Agent] = [
    Agent(
        name="Research Agent",
        description='''An agent that can perform research tasks and return summaries. 
        "Parameters: query (str): The research query provided by the user.
        You can call call_sub_agent tool with the agent_name "Research Agent" and provide the research query in the arguments to utilize this agent for research-related tasks.''',
        tool=research_agent
    ),
]

@tool("call_sub_agent", description="You can call a specific agent listed in list_agents tool with required parameter in arguments.")
async def call_sub_agent(sub_agent_call: SubAgentCallSchema) -> str:
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
    agent = next((agent for agent in agents_list if agent.name == sub_agent_call.agent_name), None)
    if not agent:
        return f"Agent '{sub_agent_call.agent_name}' not found."
    return await agent.tool.arun(tool_input=sub_agent_call.arguments)

@tool("list_agents", description="List all available agents and tools.")
def list_agents() -> list[dict[str, str]]:
    return [{"agent_name": agent.name, "description": agent.description} for agent in agents_list]