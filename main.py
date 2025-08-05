from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from constants import constants, settings


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


@app.get("/")
def get_redirect_data_api(search_term: str):
    response = requests.get(
        constants.BASE_URL,
        params={"apiKey": settings.MAP_API_KEY, "searchTerm": search_term},
    )
    response_object = response.json()
    return response_object
