"""from phi.agent import Agent, RunResponse
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

    """

from agno.agent import Agent,RunResponse
from agno.models.google import Gemini
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv
import os

def get_medical_guidance(knowledge_base, query: str) -> str:
    load_dotenv()
    
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
    
    agent = Agent(
        model=Gemini(id="gemini-2.0-flash"),
        knowledge=knowledge_base,
        tools=[TavilyTools()],
        description="An AI-powered medication advisor that provides personalized treatment recommendations.",
        instructions=(
            "You are an Agent that provides medical treatment recommendations to the symptoms the user is possibly struggling from. So list out the necessary drugs that can cure the symptoms given"
            "When answering queries about diseases, first check the knowledge base for drugs used to treat the condition. "
            "Then, use Tavily Search to fetch alerts about drug interactions, contraindications, and safety precautions for these drugs. "
            "Ensure that the response is well-structured, first listing the recommended drugs and then summarizing any relevant warnings or precautions."
            "If the knowledge base lacks information, rely on Tavily Search to provide relevant drug details. "
            "In cases where reference data from knowledge base is unavailable, proceed directly with evidence-based recommendations of Tavily Search without acknowledging data limitations of the knowledge base."
            "Maintain seamless communication by focusing solely on available treatment information, omitting any references to data availability from knowledge base."
             "Format the response clearly and concisely. Suggest a maximum of 3-4 drugs with very concise details of the drugs. Remove asterisks and slashes from the answer and make it concise"
        ),
        markdown=True
    )
    
    response: RunResponse = agent.run(query)
    return response.content