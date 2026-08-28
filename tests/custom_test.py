import os
import unittest
from pathlib import Path

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_openai import ChatOpenAI


class Tests(unittest.TestCase):

    def test_print_method(self):

        project_root = Path(__file__).resolve().parents[2]
        load_dotenv(project_root / ".env")

        api_key = os.getenv("NVIDIA_API_KEY")

        llm = ChatNVIDIA(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=api_key,
            model="nvidia/nemotron-3-ultra-550b-a55b",
            temperature=0.1,
            max_tokens=100096,
            chat_template_kwargs={"enable_thinking":True},
        )

        agent = create_agent(
            model=llm,
            tools=[],
            system_prompt="You are helpful agent"
        )

        response = agent.invoke(
            {
                "messages": [HumanMessage(content="Hi")]
            },
            version="v2"
        )

        print(response["messages"][-1].content)




if __name__ == "__main__":
    unittest.main()
    # python -m unittest custom_test.py -v