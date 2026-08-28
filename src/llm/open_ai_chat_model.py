from langchain_openai import ChatOpenAI

from src.constant import AgentConstant


def  create_llm():

    llm = ChatOpenAI(
        base_url='http://localhost:8080',
        api_key='dummy',
        temperature=AgentConstant.TEMPERATURE,
        max_tokens=AgentConstant.MAX_TOKENS,
        extra_body={
            "chat_template_kwargs": {
                "enable_thinking": True
            },
            "reasoning_budget": 1000000
        }
    )

    return llm