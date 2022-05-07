# docker-faas Repository

Repository comparing FastAPI microservice deployed as docker image and FaaS 
built with multipass and deployed on faasd.

### Modules:
- [FaaS](#faas-module)
- [Microservice](#microservice-module)

<br>

---

# FaaS Module

### Install OpenFaaS, Multipass and crate new app

Install OpenFaaS CLI

Install multipass

Launch VM
```shell
$ multipass launch --cloud-init cloud-config.yml --name faasd
```

Export IP and OPENFAAS_URL to be able to save auth and login.

Save `basic_auth_password` for `faas-cli`
```shell
$ ssh ubuntu@$IP "sudo cat /var/lib/faasd/secrets/basic-auth-password" > basic-auth-password
```

Login
```shell
$ cat basic-auth-password | faas-cli login -s
```
Or head to `http://$IP:8080/ui/` using `admin` and `basic_auth_password`

Create new function using `faas-cli`

```shell
$ faas-cli new --lang python3 app
```

### Build, Push and Deploy

Build docker image for FaaS
```shell
$ faas-cli build -f ./app.yml
```

Push docker image do Docker Hub
```shell
$ faas-cli push -f ./app.yml
```

Deploy Faas
```shell
$ faas-cli deploy -f ./app.yml
```

### Single command to Build, Push and Deploy
```shell
$ faas-cli up -f ./app.yml
```

#### Or using Docker's Parallel build
```shell
$ faas-cli up -f ./app.yml --parallel 2
```

## Metrics
Boot into the VM, modify `/var/lib/faasd/docker_compose.yml` to expose Prometheus on all IPs (`9090:9090`).

Then, after the following commands
```shell
$ sudo systemctl daemon-reload

$ sudo systemctl restart faasd
```


You can access Prometheus at `$IP:9090`

### Grafana

After installing Grafana, you can start the server with

```shell
$ sudo systemctl start grafana-server
```

Now you can access `http://localhost:3000` logging as `admin`.

<br>

---

# Microservice Module

### Run local

```shell
$ source venv/bin/activate
```

Install FastAPI, Uvicorn and other dependencies
```shell
$ pip install -r requirements.txt
```

Run with following command
```shell
$ uvicorn app.main:app --reload --port 8081
```

### Build & Push docker image to Docker Hub

Build
```shell
$ docker build -t devgmartino/docker-app:latest .
```

Push
```shell
$ docker push devgmartino/docker-app:latest
```

### Run docker image
```shell
$ docker run -p 8081:80 devgmartino/docker-app
```

## Metrics

In order to elaborate a docker container's metrics, `Prometheus` and `cAdvisor` are needed.

First we need to create a `docker-compose.yml` that will deploy the three services:

 - Prometheus
 - cAdvisor
 - docker-app

Then, in a file called `prometheus.yml` we specify some settings for the instance to be built and
to work correctly.

Finally, run the following command to run all the containers
```shell
$ docker-compose up
```