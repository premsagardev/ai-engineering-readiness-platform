from fastapi import FastAPI
from api.health import router as health_router
from api.resume import router as resume_router

app = FastAPI()

app.include_router(health_router, prefix="/api")
app.include_router(resume_router, prefix="/api")

@app.get("/")
async def read_root():
    return {"message": "Welcome to Analyzer"}