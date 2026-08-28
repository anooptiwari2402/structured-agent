from langchain_nvidia_ai_endpoints import ChatNVIDIA
from src.constant import AgentConstant



def create_nvidia_llm():

    llm = ChatNVIDIA(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=AgentConstant.nvidia_token,
        model="nvidia/nemotron-3-ultra-550b-a55b",
        temperature=AgentConstant.TEMPERATURE,
        max_tokens=AgentConstant.MAX_TOKENS,
        timeout=AgentConstant.TIMEOUT,
    )

    return llm