import json
from difflib import SequenceMatcher


def handle(req):
    json_request = json.loads(req)
    s1 = json_request["s1"]
    s2 = json_request["s2"]
    res = SequenceMatcher(None, s1, s2).ratio()
    return json.dumps({"distance": res})
