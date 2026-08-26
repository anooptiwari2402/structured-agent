from langchain_community.tools import DuckDuckGoSearchRun


def create_tools():
    duck_duck_go = DuckDuckGoSearchRun()
    return duck_duck_go