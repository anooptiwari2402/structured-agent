import asyncio

from src.runner import run_agent

if __name__ == '__main__':

    query = input("Enter your query: ")
    asyncio.run(run_agent(query))

