#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
from os import urandom


def create_blockchain(blocks, megabytes):
    blockchain = GBlockChain(megabytes)
    for i in range(blocks - 1):
        blockchain.add_block()
    return blockchain.print_summary()


class GBlock:
    def __init__(self, prev_block_hash, block_content):
        self.prev_block_hash = prev_block_hash
        self.block_content = block_content
        self.block_data = f"{block_content} - {prev_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


class GBlockChain:
    def __init__(self, content_bytes):
        self.content_bytes = content_bytes * 1024 * 1024
        self.chain = []
        self.generate_genesis_block()

    def add_block(self):
        prev_block_hash = self.last_block().block_hash
        self.chain.append(GBlock(prev_block_hash, urandom(self.content_bytes)))

    def generate_genesis_block(self):
        self.chain.append(GBlock("0", urandom(self.content_bytes)))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Hash {i + 1}: {self.chain[i].block_hash}\n")

    def last_block(self):
        return self.chain[-1]

    def print_summary(self):
        block_size = 0
        chain_size = 0

        for i in range(len(self.chain)):
            block_size = (len(self.chain[i].block_data) + len(self.chain[i].block_hash) +
                          len(self.chain[i].block_content) + len(self.chain[i].prev_block_hash)) / 1024 / 1024
            chain_size += block_size

        return {
            "chain_len": len(self.chain),
            "block_size": '{0:.2f}'.format(block_size) + " MB",
            "total_chain_size": '{0:.2f}'.format(chain_size) + " MB"
        }
