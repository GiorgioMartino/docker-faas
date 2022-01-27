from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: int
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def get_item(item_id: int, q: Optional[str] = None):
    return {"Item ID": item_id, "Query": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"Item name": item.name, "Item ID": item_id}
