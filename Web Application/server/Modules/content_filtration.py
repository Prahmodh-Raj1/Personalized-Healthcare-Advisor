from phi.agent import Agent, RunResponse
from phi.model.google import Gemini
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

def filter_medical_response(response):
    agent = Agent(
        model = Gemini(id = 'gemini-2.0-flash'),
        description = "AI Agent to filter out content for better understanding",
        instructions = [
            "Filter out the content provided in the given query, understand it and provide a concise point-by-point response of the query. Display only the important information in the given query"
        ],
        markdown = True,
        show_tool_calls = True
    )
    resp : RunResponse = agent.run(response)
    return resp.content



