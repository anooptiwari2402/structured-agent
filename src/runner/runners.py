import logging

from langchain_core.messages import HumanMessage

from rich.markdown import Markdown
from rich.console import Console

from src.agent import create_agents


async def run_agent(query_input: str, thread_id: str):

    # logging.basicConfig(level=logging.INFO)

    agent = await create_agents()

    console = Console()

    response  = await agent.ainvoke({
        "messages":[HumanMessage(content=query_input)]
    },
        config={
            "recursion_limit": 1000,
            "configurable": {
                "thread_id": f"{thread_id}",
            },
            "max_concurrency": 30
        }
    )

    content = response["messages"][-1].content

    console.print(Markdown(content))