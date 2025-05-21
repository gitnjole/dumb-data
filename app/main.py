from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from app.lastfm import api as lastfm_api

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(lastfm_api.router, prefix="/lastfm")

@app.get("/")
async def health_check():
    return {"status": "ok"}
