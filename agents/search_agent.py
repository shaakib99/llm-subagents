from langchain.tools import tool

@tool("search_agent", description="A tool to perform search on google based on a query.")
def search_agent(query: str) -> str:
    '''This tool performs a search on google based on the provided query and returns the search results.'''
    return f"Search results for: {query}"