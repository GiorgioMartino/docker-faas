## Run local

```shell
$ source venv/bin/activate
```

Installed fastapi and uvicorn.

Run with following command
```shell
$ uvicorn app.main:app --reload --port 8080
```

## Build & Push docker image to Docker Hub

Build
```shell
$ docker build -t devgmartino/docker-app:latest .
```

Push
```shell
$ docker build -t devgmartino/docker-app:latest .
```

## Run docker image
```shell
$ docker run -p 8080:80 devgmartino/docker-app
```
