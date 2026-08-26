import logging

from langchain_core.messages import HumanMessage

from rich.markdown import Markdown
from rich.console import Console

from src.agent import create_agents


async def run_agent(query_input: str):

    # logging.basicConfig(level=logging.INFO)

    agent = await create_agents()

    console = Console()

    response  = await agent.ainvoke({
        "messages":[HumanMessage(content=query_input)]
    })

    content = response["messages"][-1].content

    console.print(Markdown(content))