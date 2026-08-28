import logging

from langchain_core.messages import HumanMessage

from rich.markdown import Markdown
from rich.console import Console

from src.agent import create_agents
from src.constant import RunnerConstant


async def run_agent(query_input: str, thread_id: str):

    # logging.basicConfig(level=logging.INFO)

    agent = await create_agents()

    console = Console()

    response  = await agent.ainvoke({
        "messages":[HumanMessage(content=query_input)]
    },
        config={
            "recursion_limit": RunnerConstant.RECURSION_DEPTH,
            "configurable": {
                "thread_id": f"{thread_id}",
            },
            "max_concurrency": RunnerConstant.MAX_CONCURRENCY,
        }
    )

    content = response["messages"][-1].content

    console.print(Markdown(content))