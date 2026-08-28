import asyncio
import uuid
from pathlib import Path

from src.runner import run_agent

if __name__ == '__main__':

    # query = input("")
    # query = input("Enter your query: ")
    # if query == "exit":
    thread_id = str(uuid.uuid4())
    path = Path("/Users/anooptiwari/Downloads/workspace/pycharm-workspace/langgraph-playground/src/prompts/input.txt")
    input_query = path.read_text(encoding="utf-8")
    asyncio.run(run_agent(input_query, thread_id))

