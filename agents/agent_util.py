from langchain.tools import BaseTool, tool
from agents.research_agent import research_agent
from llm_service.models import Agent

agents_list: list[Agent] = [
    Agent(
        name="Research Agent",
        description="An agent that can perform research tasks and return summaries.",
        tool=research_agent
    ),
]

@tool("get_agent", description="Get an agent by name.")
def get_agent(name: str) -> BaseTool | None:
    return next((agent.tool for agent in agents_list if agent.name == name), None)

@tool("list_agents", description="List all available agents and tools.")
def list_agents() -> list[tuple[str, str]]:
    return [(agent.name, agent.description) for agent in agents_list]