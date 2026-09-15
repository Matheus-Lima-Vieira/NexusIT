from fastapi import FastAPI
from app.routes.chamados import router as chamados_router

app = FastAPI()
app.include_router(chamados_router)

@app.get("/")
def home():
    return {"message": "Nexus IT API"}
