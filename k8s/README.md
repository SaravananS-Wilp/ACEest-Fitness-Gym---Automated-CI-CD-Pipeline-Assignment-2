# Kubernetes Deployment Guide

This document explains how to deploy the ACEest Fitness application using Kubernetes.

## Prerequisites

- `kubectl` installed and configured
- A Kubernetes cluster available (Minikube, Docker Desktop, or cloud provider)
- Docker image built and pushed to a registry, or available in your local cluster

## Standard Deployment

Apply the service and deployment manifests:

```bash
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/deployment.yaml
```

Verify the deployment:

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

## Blue/Green Deployment

Use two separate deployments and switch traffic with the service selector.

```bash
kubectl apply -f k8s/blue-green.yaml
```

To switch traffic from blue to green, update the service selector:

```bash
kubectl patch service aceest-fitness-bluegreen --type='json' -p='[{"op":"replace","path":"/spec/selector/version","value":"green"}]'
```

## Canary Deployment

Deploy the stable set and canary release in parallel.

```bash
kubectl apply -f k8s/canary.yaml
```

Monitor canary performance and adjust traffic routing as needed.

## Rolling Update

Use the rolling update deployment manifest for zero-downtime updates.

```bash
kubectl apply -f k8s/rolling-update.yaml
```

## A/B Testing

Deploy both variants and route traffic through the service.

```bash
kubectl apply -f k8s/ab-test.yaml
```

For A/B traffic splitting, add an ingress controller or a service mesh.

## Minikube Notes

Start Minikube and enable registry access:

```bash
minikube start
minikube addons enable ingress
```

Load the local Docker image into Minikube:

```bash
minikube image load aceest-fitness:latest
```

Then apply the manifests.
