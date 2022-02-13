# Docker

*The following CPU and Memory stats have been found from Pseudo-files of the Docker Container, while the AVG Response
Time has been measured on the Client*

*These values have been taken right before/after running the Script*

```shell
$ cat /sys/fs/cgroup/cpuacct/docker/<CONTAINER_ID>/cpuacct.stat
```

```shell
$ cat /sys/fs/cgroup/memory/docker/<CONTAINER_ID>/memory.usage_in_bytes
```

# FaaS

*The following CPU and Memory stats have been found from Pseudo-files of the `faasd` Instance, while the AVG Response
Time has been measured on the Client.*

*These values have been taken right before/after running the Script*

```shell
$ cat /sys/fs/cgroup/cpu,cpuacct/openfaas-fn/<FUNCTION_NAME>/cpuacct.stat
```

```shell
$ cat /sys/fs/cgroup/memory/openfaas-fn/<FUNCTION_NAME>/memory.usage_in_bytes
```

# String Distance

### Before/After 100 request with 1-second sleep

## Docker

User CPU usage time = 136

System CPU usage time = 7

Total memory used = 0.85 MB

Avg Docker response time = 0.0143 s

## FaaS

User CPU usage time = 922

System CPU usage time = 332

Total memory used = 6.72 MB

Avg FaaS response time = 0.1866 s

# Blockchain

### Before and after 100 request, 1-second sleep

Each Post will trigger the build of a new Blockchain of `blocks` Blocks and with content size
`contet_mb`. The total size of each Block will be a little less than 4-times the content size.

Avg Block size with 1 MB content = 3.82 MB

Request body:

```json
{
  "blocks": 10,
  "content_mb": 1
}
```

## Docker

User CPU usage time = 2167

System CPU usage time = 3238

Total memory used = 0.14 MB

Avg Docker response time = 0.5464 s

## FaaS

User CPU usage time = 2690

System CPU usage time = 3079

Total memory used = 4.25 MB

Avg FaaS response time = 0.6020 s
