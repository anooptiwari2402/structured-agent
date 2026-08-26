from langchain_openai import ChatOpenAI


def  create_llm():
    llm = ChatOpenAI(
        base_url='http://localhost:8080',
        api_key='dummy',
    )
    return llm