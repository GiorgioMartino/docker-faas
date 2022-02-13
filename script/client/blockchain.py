#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import requests

docker_url = "http://127.0.0.2:8081/blockchain"
faas_url = "http://10.152.194.223:8080/function/blockchain"
docker_req_time = []
faas_req_time = []

for i in range(1, 100):
    payload = {"blocks": 10, "content_mb": 1}
    print("Sending request ", i)

    docker_start = time.time()
    requests.post(docker_url, json=payload)
    docker_end = time.time()
    docker_req_time.append(docker_end - docker_start)

    faas_start = time.time()
    requests.post(faas_url, json=payload)
    faas_end = time.time()
    faas_req_time.append(faas_end - faas_start)

    time.sleep(1)

print("Avg Docker response time = ", sum(docker_req_time) / len(docker_req_time))
print("Avg FaaS response time = ", sum(faas_req_time) / len(faas_req_time))
