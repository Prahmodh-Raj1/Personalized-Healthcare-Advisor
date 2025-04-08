"""from phi.agent import Agent, RunResponse
from phi.model.google import Gemini
from phi.tools.tavily import TavilyTools
import networkx as nx
from dotenv import load_dotenv
import os
import logging

def initialize_symptom_detector():
    # Configure logging to suppress warnings
    logging.getLogger('absl').setLevel(logging.ERROR)
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    load_dotenv()

    # Access API keys
    TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    nx_graph = nx.read_graphml("./Knowledge_graph/knowledge_graph_symptoms.graphml")
    
    graph_str_list = []
    graph_str_list.append("Nodes:\n")
    for node in nx_graph.nodes(data=True):
        graph_str_list.append(f"{node}\n")

    graph_str_list.append("\nEdges:\n")
    for edge in nx_graph.edges(data=True):
        graph_str_list.append(f"{edge}\n")

    knowledge_graph_text = "".join(graph_str_list)
    
    agent = Agent(
        model=Gemini(id="gemini-2.0-flash"),
        tools=[TavilyTools()],
        description="An AI-powered symptom analyzer that provides differential diagnoses and recommended medical actions.",
        instructions=[
            "You are an AI medical assistant that provides users with a preliminary differential diagnosis and recommended medical actions.",
            "You have access to a medical Knowledge Graph that maps symptoms to possible conditions.",
            "You also have access to the Tavily search tool to retrieve real-time medical advice and recommendations.",
            "When given symptoms, follow these steps:",
            "1. Identify possible medical conditions based on the Knowledge Graph.",
            "2. Use Tavily to retrieve recommended actions (e.g., tests, treatments, or doctor consultations).",
            "3. Generate a concise response combining both aspects, ensuring clarity in about 2-3 sentences.",
            f"Here is the structured medical Knowledge Graph data you should use:\n\n{knowledge_graph_text}\n\nUse this knowledge before making any diagnoses."
        ],
        markdown=True,
        show_tool_calls=True,
    )
    return agent

def get_symptom_analysis(symptoms):
   
    agent = initialize_symptom_detector()
    response: RunResponse = agent.run(symptoms)
    return response.content"""

import os
import logging
import networkx as nx
from dotenv import load_dotenv
from agno.agent import Agent,RunResponse
from agno.models.google import Gemini
from agno.tools.tavily import TavilyTools

def initialize_symptom_detector():
    # Configure logging to suppress warnings
    logging.getLogger('absl').setLevel(logging.ERROR)
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    load_dotenv()

    # Access API keys
    TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    nx_graph = nx.read_graphml("./Knowledge_graph/knowledge_graph_symptoms.graphml")
    
    graph_str_list = []
    graph_str_list.append("Nodes:\n")
    for node in nx_graph.nodes(data=True):
        graph_str_list.append(f"{node}\n")

    graph_str_list.append("\nEdges:\n")
    for edge in nx_graph.edges(data=True):
        graph_str_list.append(f"{edge}\n")

    knowledge_graph_text = "".join(graph_str_list)
    
    agent = Agent(
        model=Gemini(id="gemini-2.0-flash"),
        tools=[TavilyTools()],  # Add TavilyTools t
        description="An AI-powered symptom analyzer that provides differential diagnoses and recommended medical actions.",
        instructions=[
            "You are an AI medical assistant that provides users with a preliminary differential diagnosis and recommended medical actions.",
            "You have access to a medical Knowledge Graph that maps symptoms to possible conditions.",
            "You also have access to the Tavily search tool to retrieve real-time medical advice and recommendations.",
            "When given symptoms, follow these steps:",
            "1. Identify possible medical conditions based on the Knowledge Graph.",
            "2. Use Tavily to retrieve recommended actions (e.g., tests, treatments, or doctor consultations).",
            "3. Generate a brief response of 5-6 sentences combining both aspects. Display only the list of detailed top 4-5 Possible Diseases that these symptoms might cause, and do not include any recommendation",
            f"Here is the structured medical Knowledge Graph data you should use:\n\n{knowledge_graph_text}\n\nUse this knowledge before making any diagnoses."
        ],
        markdown=True
    )
    return agent

def get_symptom_analysis(symptoms):
    """
    Analyze symptoms and return medical advice
    
    Args:
        symptoms (str): Description of symptoms
    
    Returns:
        str: Medical analysis and recommendations
    """
    agent = initialize_symptom_detector()
    response: RunResponse  = agent.run(symptoms)
    return response.content