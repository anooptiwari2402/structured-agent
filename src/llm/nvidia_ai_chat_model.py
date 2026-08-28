from pathlib import Path

from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA
import os


def create_nvidia_llm():

    project_root = Path(__file__).resolve().parents[2]
    load_dotenv(project_root / ".env")

    api_key = os.getenv("NVIDIA_API_KEY")

    llm = ChatNVIDIA(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=api_key,
        model="nvidia/nemotron-3-ultra-550b-a55b",
        temperature=0.1,
        max_tokens=100096,
        # chat_template_kwargs={"enable_thinking":True},
    )

    return llm