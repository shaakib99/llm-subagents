from langchain.tools import BaseTool, tool
from agents.search_agent import search_agent

agents_list: list[BaseTool] = [
    search_agent
]

@tool("main_agent", description="The main agent that can use various tools and other agents to perform tasks.")
def main_agent(task: str) -> str:
    '''This is the main agent that can use various tools and other agents to perform tasks.'''
    # Here you can implement the logic to decide which tool or agent to use based on the task.
    # For simplicity, we will just call the search_agent for any task.
    return search_agent(task)