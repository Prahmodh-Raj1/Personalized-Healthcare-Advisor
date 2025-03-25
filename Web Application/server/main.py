from fastapi import FastAPI, Body
from Modules.symptom_detection import get_symptom_analysis
from Modules.content_filtration import filter_medical_response
from fastapi.middleware.cors import CORSMiddleware
from phi.knowledge.pdf import PDFKnowledgeBase
from phi.vectordb.lancedb import LanceDb, SearchType
from phi.embedder.google import GeminiEmbedder
from Modules.Personalised_Medication.med_guidance import get_medical_guidance
from dotenv import load_dotenv
import os


load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
knowledge_base = PDFKnowledgeBase(
    path="./Modules/Personalised_Medication/medical_conditions_and_drugs.pdf",
    vector_db=LanceDb(
        table_name="medconditions",
        uri="tmp/lancedb",
        search_type=SearchType.vector,
        embedder=GeminiEmbedder(dimensions=768),
    ),
)
knowledge_base.load()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello world"}

@app.get('/guidance')
def symptom_check(request):
    
        analysis = get_symptom_analysis(request)
        filtered_analysis = filter_medical_response(analysis)
        
        req_guidance = filtered_analysis + ". How do I cure these diseases mentioned?"
        guidance = get_medical_guidance(knowledge_base,req_guidance)
        filtered_guidance = filter_medical_response(guidance)
        
        return analysis,filtered_guidance
    