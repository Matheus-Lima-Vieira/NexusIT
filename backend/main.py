from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth import router as auth_router
from app.routes.chamados import router as chamados_router
from app.routes.usuarios import router as usuarios_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chamados_router)
app.include_router(auth_router)
app.include_router(usuarios_router)


@app.get("/")
def home():
    return {"message": "Nexus IT API"}
