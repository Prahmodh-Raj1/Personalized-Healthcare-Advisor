# Personalized-Healthcare-Advisor

### The Problem It Solves
This project provides  an AI-driven assistant that makes it easier for users to interpret their symptoms, receive personalized treatment recommendations, and obtain long-term health and lifestyle advice. It makes access to credible medical knowledge easier through large language models, real-world clinical knowledge, and web search. The aim is to enable users to make healthy decisions prior to consulting a physician.

### Description of Modules

#### 1. Symptom Assessment & Differential Diagnosis Module

This module utilizes a medical-trained LLM and a structured Knowledge Graph to interpret user symptoms, assess risk factors, and generate a ranked list of possible diagnoses. The Knowledge Graph supports accurate symptom-disease associations and personalized analysis based on age, gender, and medical history.

#### 2. Personalized Treatment & Medication Guidance Module

An Agentic Retrieval-Augmented Generation (RAG) system powers this module, providing treatment and medication suggestions based on the diagnosis and patient history. It ensures safe and context-aware recommendations by cross-referencing medical documents and evidence-based treatment protocols.

#### 3. Long-Term Lifestyle & Preventive Care Module

This module employs an AI Agent enhanced with Tavily web search to provide personalized lifestyle, diet, and wellness recommendations. It offers actionable guidance by combining AI reasoning with up-to-date information from reliable medical sources and health guidelines.

### Tech Stack Used

- React + TS

- FastAPI

- AgnoAI

- LlamaIndex

- PydanticAI

- TavilySearch

- LanceDB
