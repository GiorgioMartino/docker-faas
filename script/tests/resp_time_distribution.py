#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import time
import string
import random
from datetime import datetime
import requests

docker_distance_url = "http://127.0.0.2:8081/distance"
faas_distance_url = "http://10.52.144.99:8080/function/app"
docker_blockchain_url = "http://127.0.0.2:8081/blockchain"
faas_blockchain_url = "http://10.52.144.99:8080/function/blockchain"
docker_blockchain_req_time = []
faas_blockchain_req_time = []
docker_distance_req_time = []
faas_distance_req_time = []

for i in range(0, 1000):
    # DISTANCE
    len1 = random.randint(10000, 11000)
    len2 = random.randint(10000, 11000)
    s1 = ''.join(random.choices(string.ascii_lowercase, k=len1))
    s2 = ''.join(random.choices(string.ascii_lowercase, k=len2))
    distance_payload = {"s1": s1, "s2": s2}

    now = datetime.now().time()
    print(f"{now} - Sending request {i} for Docker Distance")
    docker_distance_start = time.time()
    requests.get(docker_distance_url, json=distance_payload)
    docker_distance_end = time.time()
    docker_distance_req_time.append(docker_distance_end - docker_distance_start)

    now = datetime.now().time()
    print(f"{now} - Sending request {i} for Faasd Distance")
    faas_distance_start = time.time()
    requests.get(faas_distance_url, json=distance_payload)
    faas_distance_end = time.time()
    faas_distance_req_time.append(faas_distance_end - faas_distance_start)

    # BLOCKCHAIN
    blockchain_payload = {"blocks": 20, "content_mb": 2}

    now = datetime.now().time()
    print(f"{now} - Sending request {i} for Docker Blockchain")
    docker_blockchain_start = time.time()
    requests.post(docker_blockchain_url, json=blockchain_payload)
    docker_blockchain_end = time.time()
    docker_blockchain_req_time.append(docker_blockchain_end - docker_blockchain_start)

    now = datetime.now().time()
    print(f"{now} - Sending request {i} for Faasd Blockchain")
    faas_blockchain_start = time.time()
    requests.post(faas_blockchain_url, json=blockchain_payload)
    faas_blockchain_end = time.time()
    faas_blockchain_req_time.append(faas_blockchain_end - faas_blockchain_start)

    time.sleep(1)

with open('../results/resp_time_distribution.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(["docker-distance",
                    "faasd-distance",
                    "docker-blockchain",
                    "faasd-blockchain"])
    for i in range(0, len(docker_distance_req_time)):
        write.writerow([docker_distance_req_time[i],
                        faas_distance_req_time[i],
                        docker_blockchain_req_time[i],
                        faas_blockchain_req_time[i]])
