from fastapi import FastAPI

from app.routers import caregivers
from app.routers.users import router as users_router

from app.database.database import engine, Base

from app.models.user_model import User
from app.models.caregiver_model import Caregiver
# Create tables

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "CareOS backend running 🚀"}


@app.get("/health")
def health_check():
    return {"status": "CareOS healthy"}


# Include routers
app.include_router(caregivers.router)
app.include_router(users_router)