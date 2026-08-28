import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient


async def create_mcps():

    project_root = Path(__file__).resolve().parents[2]
    load_dotenv(project_root / ".env")

    api_key = os.getenv("TAVILY_API_KEY")

    folder_path="/Users/anooptiwari/Downloads/workspace/pycharm-workspace/langgraph-playground/llm-model"

    mcp = MultiServerMCPClient(
        {
            "filesystem": {
                "command": "npx",
                "args": [
                    "-y",
                    "@modelcontextprotocol/server-filesystem",
                    f'{folder_path}'
                ],
                "transport": "stdio"
            },
            "terminal": {
                "command": "npx",
                "args": [
                    "@dillip285/mcp-terminal",
                    "--allowed-paths",
                    f'{folder_path}'
                ],
                "transport": "stdio"
            },
            "playwright": {
                "command": "npx",
                "args": [
                    "@playwright/mcp@latest",
                    "--browser=firefox"
                ],
                "transport": "stdio"
            },
            "tavily-remote": {
                "command": "npx",
                "args": [
                    "-y",
                    "mcp-remote",
                    f"https://mcp.tavily.com/mcp/?tavilyApiKey={api_key}"
                ],
                "transport": "stdio"
            },
            "growwmcp": {
                "command": "npx",
                "args": [
                    "mcp-remote@0.1.18",
                    "https://mcp.groww.in/mcp",
                    "52155"
                ],
                "transport": "stdio"
            },
        }
    )

    mcp_tools = await mcp.get_tools()
    return mcp_tools