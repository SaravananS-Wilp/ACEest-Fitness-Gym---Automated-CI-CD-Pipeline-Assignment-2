# ACEest Fitness & Gym DevOps Assignment Report

## CI/CD Architecture Overview

The ACEest Fitness DevOps solution is designed as an end-to-end pipeline with the following stages:

1. Version Control
   - Source code is stored in Git with a structured folder layout.  Versioned application artifacts are represented in `versions/`.
2. Build Automation
   - Python dependencies are declared in `requirements.txt` and installed as part of CI.
3. Unit Testing
   - Pytest validates API endpoints and application behavior in `tests/test_app.py`.
4. Static Code Analysis
   - SonarQube configuration is provided in `sonar-project.properties` to enforce code quality and coverage expectations.
5. Containerization
   - The `Dockerfile` packages the Flask application into a reusable image.
6. Continuous Delivery
   - A declarative `Jenkinsfile` orchestrates build, test, analysis, container build, push, and Kubernetes deployment.
7. Deployment Strategies
   - Kubernetes manifests in `k8s/` support rolling updates, blue/green deployment, canary releases, and A/B testing.

## Implementation Details

### Application Design

The Flask app exposes REST endpoints for members, workouts, bookings, health, and service metrics.  It is built with a modular factory pattern in `ACEest_Fitness.py` that supports a clean test lifecycle.

### Test Automation

Pytest is used to exercise essential API flows:

- Home route validation
- Member listing
- Workout catalog retrieval
- Booking creation
- Health checks

Automated tests are integrated into the Jenkins pipeline and report results in JUnit XML format.

### Containerization

The container image is built using a lightweight Python base image and includes the Flask application and version history.  The container is engineered for portability and can be published to Docker Hub or a private registry.

### Kubernetes Deployment

Deployment manifests are included for common DevOps release patterns:

- Standard deployment/service in `k8s/deployment.yaml` and `k8s/service.yaml`
- Blue/green deployment in `k8s/blue-green.yaml`
- Canary release in `k8s/canary.yaml`
- Rolling update strategy in `k8s/rolling-update.yaml`
- A/B testing variant rollout in `k8s/ab-test.yaml`

## Challenges and Mitigation

### Challenge: Infrastructure Dependencies

SonarQube and Kubernetes are external systems that require separate infrastructure.  The Jenkins pipeline is written to integrate with them, while still remaining portable so it can be adapted to local Minikube or cloud clusters.

### Challenge: Version Management

Maintaining multiple application versions is solved by including `versions/ACEest_Fitness_v1.py` and `versions/ACEest_Fitness_v2.py`.  These files show incremental functionality growth while preserving the base application.

### Challenge: Pipeline Portability

The `Jenkinsfile` uses standard shell commands and credential references so it can be executed on any Jenkins agent with Docker and Kubernetes CLI access.

## Key Automation Outcomes

- Automated unit testing and regression coverage for the Flask backend.
- Container image build and publish steps for repeatable deployments.
- Pipeline design that enforces code quality with SonarQube.
- Multiple Kubernetes deployment strategies for controlled release and rollback.
- A clean project structure that supports collaborative Git-driven development.

## Notes for Execution

- Replace `your-dockerhub-username` in `Jenkinsfile` and Kubernetes manifests with the actual Docker Hub repository path.
- Provide Jenkins credentials for Docker Hub and SonarQube access.
- Ensure Kubernetes context is configured before running `kubectl apply`.
