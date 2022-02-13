import json
from . import blockchain


def handle(req):
    json_req = json.loads(req)
    blocks = json_req["blocks"]
    content_mb = json_req["content_mb"]
    return json.dumps(blockchain.create_blockchain(blocks,
                                                   content_mb))
