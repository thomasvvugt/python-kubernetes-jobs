# Jobs in Kubernetes using Python
This repository contains a simple Python script that can run batch jobs using the Kubernetes API.

## Prerequirements
- Have a Kubernetes cluster

## Steps to run
1. Build the container image using `docker build -t my-python-image .`

_This image will be used to deploy the app.py script in your cluster, using `manifests.yml`_

2. Deploy this container and the related RBAC config on your cluster using `kubectl apply -f manifests.yml`
