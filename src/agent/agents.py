from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

from src.llm import create_llm, create_nvidia_llm
from src.mcp import create_mcps
from src.prompts import SYSTEM_PROMPT
from src.tools import create_tools


async def create_agents():

    mcp_tools = await create_mcps()

    agent = create_agent(
        model=create_nvidia_llm(),
        tools=[create_tools(), *mcp_tools],
        system_prompt = SYSTEM_PROMPT,
        checkpointer= InMemorySaver()
    )

    return agent