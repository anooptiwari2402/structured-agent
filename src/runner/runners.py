from langchain_core.messages import HumanMessage
from src.agent import create_agents


async def run_agent(input: str):

    agent = await create_agents()

    response  = agent.invoke({
        "messages":[HumanMessage(content=input)]
    })

    print(response["messages"][-1].content)