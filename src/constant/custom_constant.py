import os
from pathlib import Path

from dotenv import load_dotenv


project_root = Path(__file__).resolve().parents[2]
load_dotenv(project_root / ".env")


class AgentConstant:
    MAX_TOKENS = 16384
    TIMEOUT = 1000000
    TEMPERATURE = 1
    nvidia_token = os.getenv("NVIDIA_API_KEY")


class RunnerConstant:
    RECURSION_DEPTH = 100
    MAX_CONCURRENCY = 30


class McpConstant:

    tavily_token = os.getenv("TAVILY_API_KEY")
    folder_path = project_root / "llm-model"
