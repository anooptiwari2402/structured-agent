from langchain_openai import ChatOpenAI


def  create_llm():

    llm = ChatOpenAI(
        base_url='http://localhost:8080',
        api_key='dummy',
        temperature=0.1,
        max_tokens=100096,
        extra_body={
            "chat_template_kwargs": {
                "enable_thinking": True
            },
            "reasoning_budget": 1000000
        }
    )

    return llm