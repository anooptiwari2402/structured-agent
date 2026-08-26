from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchRun

from src.llm import create_llm
from src.mcp import create_mcps
from src.prompts import SYSTEM_PROMPT
from src.tools import create_tools


def create_agents():

    agent = create_agent(
        model=create_llm(),
        tools=[create_tools()],
        system_prompt = SYSTEM_PROMPT
    )

    return agent