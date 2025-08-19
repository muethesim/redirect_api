from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.api import router as app_router

app = FastAPI(
    title="Redirect API",
    version="v1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["*"],
)

app.include_router(app_router)
