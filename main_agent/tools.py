from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool

# Initialize the search tool
search_tool = DuckDuckGoSearchRun()

@tool
def web_search(query: str):
    """
    Useful for searching the internet for up-to-date information.
    Use this to find facts, recent events, or specific details.
    """
    print(f"    🔎 Scout is looking up: '{query}'...")
    return search_tool.run(query)

@tool
def save_to_file(content: str, filename: str = "research_report.md"):
    """
    Saves the final report to a markdown file.
    """
    with open(filename, "w") as f:
        f.write(content)
    print(f"    💾 Scribe saved report to {filename}")
    return "File saved successfully."
