#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import time
import requests

docker_url = "http://127.0.0.2:8081/blockchain"
faas_url = "http://10.52.144.99:8080/function/blockchain"
docker_req_time = []
faas_req_time = []

for i in range(0, 25):
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

    time.sleep(10)

with open('../results/blockchain_response_time.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(["docker", "faasd"])
    for i in range(0, len(docker_req_time)):
        write.writerow([docker_req_time[i], faas_req_time[i]])
