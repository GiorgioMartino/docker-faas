## Before/After 100 request with 1-second sleep

### Docker

*The following CPU and Memory stats have been found from Pseudo-files of the Docker Container,
while the AVG Response Time has been measured on the Client*

*These values have been taken right before/after running the Script*

```shell
$ cat /sys/fs/cgroup/cpuacct/docker/$CONTAINER_ID/cpuacct.stat
```

User CPU usage time = 136

System CPU usage time = 7

```shell
$ cat /sys/fs/cgroup/memory/docker/$CONTAINER_ID/memory.usage_in_bytes
```

Total memory used = 0.85 MB

Avg Docker response time =  0.0143 s

### FaaS

*The following CPU and Memory stats have been found from Pseudo-files of the `faasd` Instance,
while the AVG Response Time has been measured on the Client.*

*These values have been taken right before/after running the Script*

```shell
$ cat /sys/fs/cgroup/cpu,cpuacct/openfaas-fn/app/cpuacct.stat
```

User CPU usage time = 922

System CPU usage time = 332

```shell
$ cat /sys/fs/cgroup/memory/openfaas-fn/app/memory.usage_in_bytes
```

Total memory used = 6.72 MB

Avg FaaS response time =  0.1866 s
