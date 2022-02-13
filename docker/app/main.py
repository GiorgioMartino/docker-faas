#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI
from pydantic import BaseModel
from difflib import SequenceMatcher
from . import blockchain

app = FastAPI()


class DistanceData(BaseModel):
    s1: str
    s2: str


class ChainData(BaseModel):
    blocks: int
    content_mb: int


@app.get("/distance")
def compute_dist(dist_data: DistanceData):
    res = SequenceMatcher(None, dist_data.s1,
                          dist_data.s2).ratio()
    return {"distance": res}


@app.post("/blockchain")
def get_blockchain(chain_data: ChainData):
    return blockchain.create_blockchain(chain_data.blocks,
                                        chain_data.content_mb)
