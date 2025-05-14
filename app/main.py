from fastapi import FastAPI
from app.lastfm import api as lastfm_api

app = FastAPI()
app.include_router(lastfm_api.router, prefix="/lastfm")
@app.get("/")
async def health_check():
    return {"status": "ok"}
