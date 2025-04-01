from agno.agent import Agent,RunResponse
from agno.models.google import Gemini
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

def filter_medical_response(response):
    agent = Agent(
        model=Gemini(id="gemini-2.0-flash"),
        description="AI Agent to filter out content for better understanding",
        instructions=[
            "Filter out the content provided in the given query, understand it and provide a concise point-by-point response of the query.",
            "Display only the important information in the given query"
        ],
        markdown=True
    )
    
    filtered_response: RunResponse = agent.run(response)
    return filtered_response.content



