from typing import Union

from fastapi import FastAPI
import uvicorn


api = FastAPI()


@api.get("/")
async def read_root():
    return {"Hello": "World"}


@api.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def start():
    uvicorn.run("app:api", host="0.0.0.0", port=8000, reload=True)
