from fastapi import FastAPI, Body
from Modules.symptom_detection import get_symptom_analysis
from Modules.lifestyle_care import get_lifestyle_recommendations
from Modules.content_filtration import filter_medical_response
from request_models import SymptomRequest, MedGuidanceRequest, LifeStyleGuidanceRequest
from fastapi.middleware.cors import CORSMiddleware
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.embedder.google import GeminiEmbedder
from pydantic import BaseModel, field_validator, model_validator
from Modules.Personalised_Medication.med_guidance import get_medical_guidance
from dotenv import load_dotenv
import os


load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
knowledge_base = PDFKnowledgeBase(
    path="./Modules/Personalised_Medication/medical_conditions_and_drugs.pdf",
    vector_db=LanceDb(
        table_name="medconditions",
        uri="tmp/lancedb/work",
        search_type=SearchType.vector,
        embedder=GeminiEmbedder(),
    ),
)
knowledge_base.load()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://localhost:5173","http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Health Advisory App"}



@app.post('/symptoms')
async def symptom_check(request: SymptomRequest):
    try:
        analysis = get_symptom_analysis(request.symptoms)
        filtered_analysis = filter_medical_response(analysis)
        return filtered_analysis
    except Exception as e:
        return {"error": str(e)}

@app.post('/med_guidance')
async def med_guidance(request : MedGuidanceRequest):
    try:
        req_guidance = request.analysis + ". How do I cure these diseases mentioned?"
        guidance = get_medical_guidance(knowledge_base, req_guidance)
        filtered_guidance = filter_medical_response(guidance)

        return filtered_guidance
    except Exception as e:
        return {"error": str(e)}

@app.post('/lifestyle')
async def lifestyle(request : LifeStyleGuidanceRequest):
    try:
        filtered_req = request.analysis + request.guidance
        lifestyle_guidance = get_lifestyle_recommendations(filtered_req)
        filtered_lifestyle_guidance = filter_medical_response(lifestyle_guidance)
        
        return filtered_lifestyle_guidance
    except Exception as e:
        return {"error": str(e)}
        