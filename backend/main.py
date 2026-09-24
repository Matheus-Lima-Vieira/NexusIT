from fastapi import FastAPI

from app.routes.auth import router as auth_router
from app.routes.chamados import router as chamados_router
from app.routes.usuarios import router as usuarios_router

app = FastAPI()

app.include_router(chamados_router)
app.include_router(auth_router)
app.include_router(usuarios_router)


@app.get("/")
def home():
    return {"message": "Nexus IT API"}
