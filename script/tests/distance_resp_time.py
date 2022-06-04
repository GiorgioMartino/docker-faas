#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import time
import string
import random

import requests

docker_url = "http://127.0.0.2:8081/distance"
faas_url = "http://10.52.144.99:8080/function/app"
docker_req_time = []
faas_req_time = []

for i in range(0, 25):
    len1 = random.randint(10000, 11000)
    len2 = random.randint(10000, 11000)
    s1 = ''.join(random.choices(string.ascii_lowercase, k=len1))
    s2 = ''.join(random.choices(string.ascii_lowercase, k=len2))
    payload = {"s1": s1, "s2": s2}
    print("Sending request ", i)

    docker_start = time.time()
    requests.get(docker_url, json=payload)
    docker_end = time.time()
    docker_req_time.append(docker_end - docker_start)

    faas_start = time.time()
    requests.get(faas_url, json=payload)
    faas_end = time.time()
    faas_req_time.append(faas_end - faas_start)

    time.sleep(10)

with open('../results/distance_response_time.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(["docker", "faasd"])
    for i in range(0, len(docker_req_time)):
        write.writerow([docker_req_time[i], faas_req_time[i]])
