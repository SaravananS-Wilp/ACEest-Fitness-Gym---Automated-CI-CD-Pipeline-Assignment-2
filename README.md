# ACEest Fitness & Gym DevOps Pipeline

This repository contains a sample fitness management Flask application and a simulated industry-grade DevOps pipeline for ACEest Fitness & Gym.

## Contents

- `ACEest_Fitness.py` - Primary Flask application.
- `versions/ACEest_Fitness_v1.py` and `versions/ACEest_Fitness_v2.py` - Versioned application variants.
- `requirements.txt` - Python dependencies.
- `Dockerfile` - Container build instructions.
- `Jenkinsfile` - Declarative Jenkins pipeline.
- `sonar-project.properties` - SonarQube static analysis configuration.
- `tests/` - Pytest unit tests and fixtures.
- `k8s/` - Kubernetes manifests for standard deployment, blue/green, canary, rolling update, and A/B testing.
- `REPORT.md` - Assignment rationale, architecture, and outcomes.

## How to run locally

1. Create a Python virtual environment.
2. Install dependencies: `python -m pip install -r requirements.txt`
3. Run the app: `python ACEest_Fitness.py`
4. Access `http://localhost:5000/`

## Testing

Run unit tests with:

```bash
pytest
```

## Docker build

Build the container image:

```bash
docker build -t aceest-fitness:latest .
```

## Docker Compose

Run the application and SonarQube together:

```bash
docker compose up --build
```

Visit `http://localhost:5000/` for the app and `http://localhost:9000/` for SonarQube.

## GitHub Actions CI

A GitHub Actions workflow is included at `.github/workflows/ci.yml` for automated test, build, and SonarQube scan execution on `push` and `pull_request` events.

## Kubernetes deployment

Apply the standard deployment:

```bash
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/deployment.yaml
```

For blue/green, canary, rolling update, and A/B testing, apply the appropriate manifest under `k8s/`.

## Local development helper

A `docker-compose.override.yml` file is included for local development, mounting the current directory and running the app with the Flask dev server.

## Minikube bootstrap script

Use `scripts/minikube-bootstrap.ps1` to start Minikube, enable ingress, load the local Docker image, and deploy the standard Kubernetes manifests.
