from fastapi import FastAPI, Body
from Modules.symptom_detection import get_symptom_analysis
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel



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

@app.get('/symptoms')
def symptom_check(request):
    
        analysis = get_symptom_analysis(request)
        print(analysis)
        return analysis
    