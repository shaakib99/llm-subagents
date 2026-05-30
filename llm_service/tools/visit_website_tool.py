from langchain.tools import tool
from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth

@tool("visit_website", description="A tool to visit a website and retrieve its content based on the provided URL.")
def visit_website_tool(url: str) -> str:
    '''This tool visits a website and retrieves its content based on the provided URL.'''
    
    content = ""
    # This is the recommended usage. All pages created will have stealth applied:
    with Stealth().use_sync(sync_playwright()) as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto(url)
        page.wait_for_load_state('domcontentloaded')  # Wait until the DOM is fully loaded
        content = page.content()
        browser.close()
    return f"Content from website: {url}\n{content[:1000]}..."  # Return the first 1000 characters of the website content for brevity.