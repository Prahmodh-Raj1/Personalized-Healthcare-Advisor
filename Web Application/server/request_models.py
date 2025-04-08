from pydantic import BaseModel, Field
class SymptomRequest(BaseModel):
    symptoms: str = Field(..., min_length=1)

class MedGuidanceRequest(BaseModel):
    analysis: str = Field(..., min_length=1)

class LifeStyleGuidanceRequest(BaseModel):
    analysis: str = Field(...,min_length=1)
    guidance: str = Field(...,min_length=1)