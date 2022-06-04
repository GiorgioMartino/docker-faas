#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import time

import requests
import paramiko
import os

host = "10.52.144.99"
user = "ubuntu"
faas_cmd = "cat /sys/fs/cgroup/memory/openfaas-fn/blockchain/memory.usage_in_bytes"

container_id = "77ea3fde2c023daa958347a481e0b5f6afab62187e9ebb2ffe6a1ef90887f7b8"
docker_cmd = f"cat /sys/fs/cgroup/memory/docker/{container_id}/memory.usage_in_bytes"

docker_url = "http://127.0.0.2:8081/blockchain"
faas_url = "http://10.52.144.99:8080/function/blockchain"
docker_mem = []
faas_mem = []

print("Connecting SSH...")
ssh = paramiko.SSHClient()
k = paramiko.RSAKey.from_private_key_file("id_rsa")

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username=user, pkey=k)
print("SSH Connected")

ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(faas_cmd)
ssh_out = ssh_stdout.read().decode("utf8")
faas_mem.append(ssh_out.partition("\n")[0])

out = os.popen(docker_cmd).read()
docker_mem.append(out.partition("\n")[0])

for i in range(0, 50):
    payload = {"blocks": 10, "content_mb": 1}
    print("Sending request ", i)

    requests.post(docker_url, json=payload)
    out = os.popen(docker_cmd).read()
    docker_mem.append(out.partition("\n")[0])

    requests.post(faas_url, json=payload)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(faas_cmd)
    ssh_out = ssh_stdout.read().decode("utf8")
    faas_mem.append(ssh_out.partition("\n")[0])

    time.sleep(10)

with open('../results/blockchain_memory.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(["docker", "faasd"])
    for i in range(0, len(docker_mem)):
        write.writerow([docker_mem[i], faas_mem[i]])
