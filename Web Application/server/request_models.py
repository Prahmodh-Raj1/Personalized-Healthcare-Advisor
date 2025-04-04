from pydantic import BaseModel
class SymptomRequest(BaseModel):
    symptoms: str

class MedGuidanceRequest(BaseModel):
    analysis: str

class LifeStyleGuidanceRequest(BaseModel):
    analysis: str
    guidance: str