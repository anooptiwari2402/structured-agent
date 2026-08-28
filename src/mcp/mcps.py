from langchain_mcp_adapters.client import MultiServerMCPClient
from src.constant.custom_constant import McpConstant


async def create_mcps():

    folder_path=McpConstant.folder_path

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
                    f"https://mcp.tavily.com/mcp/?tavilyApiKey={McpConstant.tavily_token}"
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