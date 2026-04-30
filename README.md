# ACEest Fitness Gym – Automated CI/CD Pipeline

## 1. Introduction

This project presents the **ACEest Fitness & Gym DevOps Pipeline**, designed to automate the software delivery lifecycle for a Flask-based fitness management application.

The pipeline integrates modern DevOps tools and practices including **Git, Jenkins, Docker, SonarQube, Pytest, and Kubernetes**. It demonstrates an end-to-end **CI/CD workflow**, covering build automation, automated testing, static code quality validation, containerization, and scalable deployment.

---

## 2. Project Overview

The repository is structured to support modular development, testing, and deployment:

### Application Layer
- `ACEest_Fitness.py` – Core Flask application
- `versions/ACEest_Fitness_v1.py`, `ACEest_Fitness_v2.py` – Versioned variants

### Dependency Management
- `requirements.txt` – Python dependencies

### Testing
- `tests/` – Pytest-based unit tests and fixtures

### Containerization
- `Dockerfile` – Application container build instructions (Gunicorn-based)

### CI/CD Pipeline
- `Jenkinsfile` – Declarative Jenkins pipeline

### Code Quality
- `sonar-project.properties` – SonarQube configuration

### Deployment
- `k8s/` – Kubernetes manifests supporting:
  - Standard deployment
  - Blue-Green deployment
  - Canary deployment
  - Rolling updates
  - A/B testing

### Automation
- `scripts/minikube-bootstrap.ps1` – Local Kubernetes setup script
- `docker-compose.override.yml` – Local development helper

---

## 3. CI/CD Architecture Overview

The architecture integrates version control, automation, and orchestration into a unified workflow.

### Version Control
- Managed using Git
- Structured repository with application code, tests, and deployment configs

### Continuous Integration
- Implemented using **Jenkins** and **GitHub Actions**
- Pipeline stages:
  - Environment setup
  - Dependency installation
  - Test execution
  - Docker image build and push

### Automated Testing
- Implemented using **Pytest**
- Covers:
  - Member APIs
  - Workout endpoints
  - Booking workflows
- Generates **JUnit XML reports**

### Static Code Quality
- Integrated with **SonarQube**
- Ensures:
  - Code maintainability
  - Reduced complexity
  - Vulnerability detection

### Containerization
- Docker-based packaging
- Uses **Gunicorn** for production runtime
- Ensures consistent execution across environments

### Orchestration
- Managed using **Kubernetes**
- Handles deployment, scaling, and service exposure

---

## 4. DevOps Pipeline Flow

1. Code commit to Git repository  
2. CI pipeline triggered (Jenkins / GitHub Actions)  
3. Dependency installation  
4. Automated testing (Pytest)  
5. Static analysis (SonarQube)  
6. Docker image build  
7. Container deployment to Kubernetes  
8. Traffic routing using deployment strategies  

---

## 5. Local Setup and Execution

### Run Application Locally

```bash
python -m pip install -r requirements.txt
python ACEest_Fitness.py
```
Access the application at:
```bash
http://localhost:5000/
```
---
## 6. Testing

Run unit tests:
```bash 
pytest
 ```
---
## 7. Docker Usage
Build Docker Image
```bash
docker build -t aceest-fitness:latest .
```
Run with Docker Compose
```bash
docker compose up --build
```
Access:
Application: http://localhost:5000/
SonarQube: http://localhost:9000/

---

## 8. Kubernetes Deployment
Standard Deployment
```bash
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/deployment.yaml
```

### Deployment Strategies
- Rolling Update – Zero downtime deployment
- Blue-Green Deployment – Instant switching between environments
- Canary Deployment – Gradual rollout to a subset of users
- A/B Testing – Traffic-based comparison between versions

---
## 9. Minikube Setup

Use the bootstrap script:
```bash
scripts/minikube-bootstrap.ps1
```

This will:
- Start Minikube
- Enable ingress controller
- Load Docker image
- Deploy Kubernetes manifests

---
## 10. Challenges & Mitigation Strategies
| Challenge                                                  | Mitigation Strategy                                                                   |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Infrastructure complexity (Jenkins, SonarQube, Kubernetes) | Used Docker Compose for standardized local setup and documented environment variables |
| Environment inconsistency                                  | Used the same Docker image across all environments and Minikube for local simulation  |
| Version management                                         | Structured version directories and semantic tagging                                   |
| SonarQube dependency in CI                                 | Used containerized SonarQube and flexible pipeline configuration                      |


---
## 11. Key Automation Outcomes
- Automated build and test execution on every commit
- Integrated static code quality validation
- Reliable API validation using Pytest
- Portable and reproducible deployments using Docker
- Scalable Kubernetes-based deployment
- Support for advanced deployment strategies
- Reduced regression risk through automated testing

---
## 12. Repository Link

GitHub Repository:
https://github.com/SaravananS-Wilp/ACEest-Fitness-Gym---Automated-CI-CD-Pipeline-Assignment-2

---
## 13. Conclusion

The ACEest Fitness & Gym DevOps pipeline demonstrates a complete implementation of modern CI/CD practices. By integrating source control, automated testing, static analysis, containerization, and Kubernetes orchestration, the project achieves a scalable and resilient delivery system.
