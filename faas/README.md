# Install OpenFaaS, Multipass and crate new app

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

## Build, Push and Deploy

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

## Single command to Build, Push and Deploy
```shell
$ faas-cli up -f ./app.yml
```
