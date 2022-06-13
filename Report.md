# Docker vs Faasd Project

The Project aims to compare two different approaches in the deployment of a web service, one using
the well established Docker, creating an image, building it into a container able to be "shipped", 
used and deployed everywhere. 

The other one is a more modern and less used approach,
Function as a Service, where each snippet of serverless function is deployed and activated on 
request.

### Modules:
- [Description and Technologies](#Description-and-Technologies)
- [Issues and Solutions](#Issues and Solutions)
- [Experiments and Results](#Experiments and Results)
- [Limitations and Future Improvements](#Limitations and Future Improvements)


## Description and Technologies

[//]: # (TODO add images)

This repository is intended to provide a comparison between two different services, implemented using
two different technologies, and benchmark those technologies.

### Technologies

As stated before, the two technologies used are Docker and FaaS.

- Docker is a *standard-de-facto* in the industry, usually a docker container is created for each
microservice. In our case only one microservice contains the logic and endpoints for both services.
- FaaS has different implementations, the chosen one is **faasd**. Provided by OpenFaaS, is 
a lightweight implementation perfect for testing and proof-of-concepts, different from the enterprise 
version which needs Kubernetes to be used.

The REST APIs have been implemented using Python FastAPI.

### Services

For the purpose of this project, two logical services have been implemented.

#### String Distance

The first one (Distance from now on) is a dummy implementation of the String Distance algorithm, 
accepting two Strings of arbitrary length and returning the computed distance value. The main point 
of this first service was to test all the infrastructure.

#### Blockchain Build

The second one was instead implemented for benchmarking purposes. That's the main reason why Blockchain
has been chosen. The service accepts two Input parameters: `blocks` and `content_mb`.

The first is the number of blocks that should constitute the chain, while the second in the size
(expressed in MegaBytes) of the block content.

Each block contains the SHA256 hash of the previous block, content, data and the hash of itself.

## Issues and Solutions

The code written to implement the services is not complex, and FastAPI in well documented.

Building a docker image requires little knowledge of the Docker ecosystem but is far from impossible,
even more because it's a single image container.

Setting up a faasd environment in not too hard either, but some problems were encountered. First of 
all the documentation in very tiny, and having it up and running on a server is probably easier. 
Due to some internal conflicts with docker, **multipass** is required (utility from Canonical).

Multipass will create a VM containing a faasd instance starting from a YAML configuration file.
Then the user is required to log into the VM, save the password in order to run CLI commands from
the faas-cli from the host OS.

Finally, one or more functions can be created, and through another YAML configuration file we can
specify each function's image name, and a base-url for all of them.

One of the biggest problems here was that, according to the documentation given by OpenFaas, it should
be possible to use images from local host, or even deploy a local registry and use it. Instead, 
no way has been proved to work except for using the official Docker Hub (luckily it's free).

Apart from that, the faas-cli allows the build, push and deploy stages of the functions in a handy 
way.

### Metrics

The other big part of this project was to find as many metrics as possible. 
Again, with Docker things went way smoother than with faasd. 

Given that both services use docker images, some useful metrics were found in the CGroup files.
For the Docker app they were in the host OS, under the container folder, while for faasd they have been
found inside the VM. Those metrics are quite simple, but very effective, especially the user/system
CPU time, and the Memory Usage in Bytes.

The easiest metric to compute was the response time.

On the other hand, some more complex and graphical metrics were experimented. 
In this case one of the standard ways to achieve that is to include Prometheus in the deployment and
expose the metrics that will then be graphically rendered through Grafana.

Again, for Docker the solution was a bit easier, even though it involved a docker-compose: deploy
an app containing not only the Docker app, but also cAdvisor and Prometheus.

faasd supports Prometheus out-of-the-box, inspired by OpenFaaS, but it has to be enabled manually.
This can be done by accessing the docker-compose file inside the VM. Even by doing that not many metrics are
available to the user, way less than those available for OpenFaas users.

The most useful metrics, as stated before, remain the simplest ones: response times, CPU usage and
memory consumption. 


## Experiments and Results

All the following experiments have been run simultaneously on both services. The goal here was to evaluate three
parameters for both Distance and Blockchain.

Keeping in mind that the Blockchain service is much more realistic than the Distance one, the first tests were
run on the response times.

### Response Time

Given the URLs (`http://127.0.0.2:8081/blockchain` for Docker and `http://10.52.144.99:8080/function/blockchain` 
for faasd), the current time in milliseconds was annotated before and after each request. The results were 
then added to a CSV file, used to create the following graphs.

<img src="script/results/graphs/String Distance - Response Time.png" width="805" height="497">

As we can see, in both cases the Docker app performs much better than faasd.

<img src="script/results/graphs/Blockchain Build - Response Time.png" width="805" height="497">


### CPU and Memory Usage

For the following metrics the approach was very similar, sending each request and annotating the current metric 
for the service, with a time sleep between requests. This worked very well also for CPU and Memory usage, because
the control groups metrics are incremental, allowing to compare the growth of the curve between Docker and faasd.

The only tweak required was to include in the scripts one shell command (for what concerns Docker metrics,
being in the host OS), and using a library to send SSH commands (to access the metrics on the faasd instance)

### CPU Usage

Here we can observe the graphs regarding the user CPU usage.

<img src="script/results/graphs/String Distance - CPU Usage.png" width="805" height="497">

Here the difference is quite big on the Distance, while considerably smaller in the Blockchain. Still Docker 
outperforms faasd.

These metrics have been scaled to have them both start at zero.

<img src="script/results/graphs/Blockchain Build - CPU Usage.png" width="805" height="497">

### Memory Usage

<img src="script/results/graphs/String Distance - Memory Usage.png" width="805" height="497">

Once again the metrics show how Docker has performed much better than faasd. 

The interesting fact is the memory management here, the Docker app is able to keep a low memory footprint, 
even while running a memory hungry service like Blockchain, while faasd cannot keep up with all the requests.

These metrics have been scaled to have them both start at zero.

<img src="script/results/graphs/Blockchain Build - Memory Usage.png" width="805" height="497">

### Distribution Fitting

Last but not least, we can see at the following [Jupyter Notebook](script/results/jupyter/jupyter.md) that the 
four different datasets regarding the response times have been plotted into histograms, and an attempt at fitting
these distributions into standard ones has been made.

For this purpose a Python library was used named `Fitter`. It's a library that runs on top of `scipy` standard 
distributions, trying to find the best matches for the given one. Due to execution times only a subset of all
standard distributions present in `scipy` have been used.

## Limitations and Future Improvements

The biggest limitation (as perceived by the maintainer) has been the usage of faasd over OpenFaas. Although OpenFaas 
is not suitable for a University project, it would be interesting to see it in action against Docker.

Another improvement to have a more fair comparison would be to use a different type of service, one that is closer 
to the capacities and strength of FaaS. As an example, a future implementation would be to develop a complex task (maybe
something that needs 5/10 minutes to run), deploy it with Docker as an always active player and OpenFaaS as an event
driven one, (imagine both on different web services, not deployed on localhost), and test the CPU and Memory usage over 
multiple days/week, calling the APIs maybe once or twice a day. That way, the FaaS implementation, even though it could be 
slightly slower, could still win in performance (intended as power usage, cloud provider overall costs etc...)
