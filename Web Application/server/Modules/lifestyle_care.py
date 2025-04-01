from phi.agent import Agent, RunResponse

from dotenv import load_dotenv
import os
import logging
from agno.agent import Agent,RunResponse
from agno.models.google import Gemini
from agno.tools.tavily import TavilyTools

def initialize_lifestyle_agent():
    # Configure logging to suppress warnings
    logging.getLogger('absl').setLevel(logging.ERROR)
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    load_dotenv()
    TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
    # Access API keys
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    
    agent = Agent(
        model=Gemini(id="gemini-2.0-flash"),
        tools=[TavilyTools()],
        description="An AI-powered lifestyle and preventive care advisor for long-term health management.",
       instructions=[
            "You are an AI health advisor that provides personalized lifestyle recommendations and preventive care advice.",
            "You have access to the Tavily search tool to retrieve evidence-based health recommendations.",
            "When given a diagnosis and treatment plan, follow these steps:",
            "1. Identify key lifestyle factors that can help manage the diagnosed condition(s).",
            "2. Use Tavily to search for evidence-based lifestyle modifications, dietary recommendations, and monitoring guidelines.",
            "3. Suggest specific, actionable lifestyle changes including diet, exercise, stress management, and sleep.",
            "4. Recommend appropriate health metrics to monitor (blood pressure, glucose, etc.) and their frequency.",
            "5. Generate a comprehensive response that combines your knowledge with search results.",
            "6. Format your response in clear sections: Diet, Exercise, Monitoring, and Additional Recommendations.",
            "Always emphasize that your advice complements but does not replace medical treatment."
        ],
        markdown=True
    )
    return agent

def get_lifestyle_recommendations(diagnosis_and_treatment):
    """
    Generate personalized lifestyle and preventive care recommendations
    
    Args:
        diagnosis_and_treatment (str): Diagnosis from symptom assessment and medication recommendations
    
    Returns:
        str: Comprehensive lifestyle and preventive care recommendations
    """
    agent = initialize_lifestyle_agent()
    response : RunResponse = agent.run(diagnosis_and_treatment)
    return response.content