from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from difflib import SequenceMatcher

app = FastAPI()


class Strings(BaseModel):
    s1: str
    s2: str


@app.get("/distance")
def compute_dist(strings: Strings):
    res = SequenceMatcher(None, strings.s1, strings.s2).ratio()
    return {"distance": res}


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def get_item(item_id: int, q: Optional[str] = None):
#     return {"Item ID": item_id, "Query": q}
#
#
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"Item name": item.name, "Item ID": item_id}
