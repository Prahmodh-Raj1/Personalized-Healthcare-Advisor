from phi.agent import Agent, RunResponse
from phi.model.google import Gemini
from phi.tools.tavily import TavilyTools
from dotenv import load_dotenv
import os

def get_medical_guidance(knowledge_base, query: str) -> str:
    load_dotenv()
    
    agent = Agent(
        model=Gemini(id="gemini-2.0-flash"),
        tools=[TavilyTools()],
        knowledge=knowledge_base,
        instructions=(
            "When answering queries about diseases, first check the knowledge base for drugs used to treat the condition. "
            "Then, use Tavily Search to fetch alerts about drug interactions, contraindications, and safety precautions for these drugs. "
            "Ensure that the response is well-structured, first listing the recommended drugs and then summarizing any relevant warnings or precautions. "
            "If the knowledge base lacks information, rely on Tavily Search to provide relevant drug details. "
            "Format the response clearly and concisely."
        ),
        show_tool_calls=True,
        markdown=True,
    )
    
    response: RunResponse = agent.run(query)
    return response.content