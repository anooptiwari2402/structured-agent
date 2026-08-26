from langchain_core.messages import HumanMessage
from src.agent import create_agents


def run_agent(input: str):
    response  = create_agents().invoke({
        "messages":[HumanMessage(content=input)]
    })

    print(response["messages"][-1].content)