from langchain.tools import tool
from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth
from bs4 import BeautifulSoup

@tool("search", description="Search using DuckDuckGo (no CAPTCHA issues)")
def search_tool(query: str) -> str:
    with Stealth().use_sync(sync_playwright()) as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"https://duckduckgo.com/?q={query}")
        page.wait_for_load_state('domcontentloaded')
        # Extract search results (for simplicity, we will just return the page content)
        content = page.content()
        soup = BeautifulSoup(content, "html.parser")
        search_results = []
        for result in soup.select(".result__title a.result__a"):
            title = result.get_text()
            link = result['href']
            search_results.append(f"{title}: {link}")
        print(f"Search results for '{query}':\n" + "\n".join(search_results[:5]))  # Print top 5 results
        browser.close()
    return content