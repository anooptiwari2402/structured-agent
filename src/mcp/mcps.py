from langchain_mcp_adapters.client import MultiServerMCPClient


async def create_mcps():

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
            }
        }
    )

    mcp_tools = await mcp.get_tools()