from langchain.tools import tool

@tool("visit_website", description="A tool to visit a website and retrieve its content based on the provided URL.")
async def visit_website_tool(url: str) -> str:
    '''This tool visits a website and retrieves its content based on the provided URL.'''
    return f"Content from website: {url}"