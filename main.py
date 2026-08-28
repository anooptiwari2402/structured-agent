import asyncio
import uuid
from pathlib import Path

from src.runner import run_agent

if __name__ == '__main__':

    print("======Start======")

    thread_id = str(uuid.uuid4())

    while True:
        query = ""
        query_input = input("Please enter your query: ")
        if query_input == "exit":
            break
        if query_input == "file":
            path = Path("input_query.txt")
            query = path.read_text(encoding="utf-8")
        else:
            query = query_input

        asyncio.run(run_agent(query, thread_id))

    print("======Done======")

