from fastapi import FastAPI
import uvicorn

from app.routes import detection

api = FastAPI()

api.include_router(detection.router)


def start():
    uvicorn.run("app:api", host="0.0.0.0", port=8000, reload=True)
