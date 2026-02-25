from pydantic import BaseModel
from fastapi import FastAPI


# Create FastAPI app
app = FastAPI()

# --------------------------------------------------------
# Root Endpoint
# -------------------------------------------------------- 
@app.get("/")
def home():
    return {"message": "CareOS backend running 🚀"}

# --------------------------------------------------------
# Health Check Endpoint
# -------------------------------------------------------- 
@app.get("/health")
def health_check():
    return {"status": "CareOS healthy"}

# --------------------------------------------------------
# Caregiver Data Model
# -------------------------------------------------------- 
class Caregiver(BaseModel):
    name: str
    email: str
    phone: str
    location: str

# --------------------------------------------------------
# Temporary Database (Memory) l
# -------------------------------------------------------- 
caregivers = []

# --------------------------------------------------------
# Register Caregiver 
# -------------------------------------------------------- 
@app.post("/caregivers")
def register_caregiver(caregiver: Caregiver):
    caregivers.append(caregiver)
    return {"message": "Caregiver registered successfully"}

# --------------------------------------------------------
# Get All Caregivers
# -------------------------------------------------------- 
@app.get("/caregivers")
def get_caregivers():
    return caregivers