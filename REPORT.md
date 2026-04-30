# ACEest Fitness & Gym DevOps Assignment Report

## Executive Summary

This report documents the ACEest Fitness DevOps pipeline, which is designed to automate software delivery for a sample fitness application using Git, Jenkins, Docker, SonarQube, Pytest, and Kubernetes. The solution demonstrates an end-to-end CI/CD workflow that includes build automation, automated testing, static code quality validation, containerization, image publishing, and Kubernetes deployment strategies for resilient application rollout.

The report is structured into three key areas: the CI/CD architecture overview, the challenges faced with mitigation strategies, and the key automation outcomes achieved by the project.

## CI/CD Architecture Overview

### Version Control and Source Management

The foundation of the pipeline is Git version control. The repository is organized into a clear application structure with the main Flask app in `ACEest_Fitness.py`, versioned application variants in `versions/`, test suites in `tests/`, configuration in `requirements.txt`, and deployment artifacts in `k8s/`.

Key practices adopted:

- Branch-based development for incremental changes.
- Semantic versioning of application builds through Docker tags.
- Separation of application code, infrastructure manifests, and pipeline configuration.

### Build Automation

Build automation is implemented through Jenkins and Docker. The Jenkins pipeline is defined declaratively in `Jenkinsfile`, providing a repeatable workflow for every commit. Major build stages include:

1. Checkout
2. Environment preparation
3. Dependency installation
4. Unit test execution
5. Static analysis scanning
6. Docker image build
7. Docker image push
8. Kubernetes deployment

The pipeline uses `requirements.txt` to install Python dependencies and relies on standard shell commands to keep the build portable across Jenkins agents.

### Automated Testing

Test automation is central to the pipeline. Pytest is used to validate the Flask application with coverage-focused tests for important endpoints and behaviors:

- Home endpoint accessibility
- Member list retrieval
- Workouts API validation
- Booking creation workflow
- Health probe response

Test artifacts are exported in JUnit XML format, enabling Jenkins to surface pass/fail results in the build UI.

### Static Code Quality

SonarQube is integrated as a quality gate to enforce maintainability and code analysis. The `sonar-project.properties` file configures the scan, targeting the application source and excluding test and deployment artifacts.

While SonarQube is run as an external service, the pipeline includes a scan stage that can be adapted to local `docker-compose` or cloud-based SonarQube instances.

### Containerization and Registry Integration

The application is packaged into a Docker container using `Dockerfile`, which installs Python dependencies and runs the Flask app under Gunicorn. The image is designed for a minimal production footprint and isolates runtime dependencies.

A Docker Compose workflow is also included for local development. The Compose setup supports the app service and a SonarQube service, enabling integration testing of the scan flow without external infrastructure.

### Deployment Strategy

Deployment to Kubernetes is automated through the pipeline. Kubernetes manifests in `k8s/` support multiple delivery strategies:

- Standard deployment and service (`deployment.yaml`, `service.yaml`)
- Rolling updates
- Blue-green deployment
- Canary release
- A/B testing rollout

This multi-strategy approach demonstrates how the same application can support gradual traffic shifts, safe cutovers, and rollback capabilities.

## Challenges Faced and Mitigation Strategies

### Challenge 1: Infrastructure Dependencies

Integrating Jenkins, SonarQube, Docker, and Kubernetes introduces infrastructure complexity. Each tool has its own runtime and configuration requirements.

Mitigation:

- Reused Docker Compose to standardize local development and SonarQube setup.
- Kept the Jenkins pipeline modular so that external services can be swapped or mocked during early-stage testing.
- Documented the required environment variables and execution order clearly in README and helper scripts.

### Challenge 2: Local Development vs. Production Parity

It is difficult to maintain consistency between local developer environments and the production deployment target.

Mitigation:

- Added `docker-compose.override.yml` for local development with mounted source code.
- Created a Minikube bootstrap script to simulate the Kubernetes environment locally.
- Used the same Docker image definition for both local and cluster deployments.

### Challenge 3: Multiple Deployment Patterns

Supporting a wide range of deployment strategies can increase configuration overhead and create management complexity.

Mitigation:

- Encapsulated each strategy into its own Kubernetes manifest file.
- Used simple selector-based service routing for blue/green and A/B testing.
- Documented the purpose and application steps for each manifest, providing a clear path for demonstration and evaluation.

### Challenge 4: Automated Quality Gates

Automating SonarQube scans without a fully configured server can make CI fragile.

Mitigation:

- Provided a Docker Compose SonarQube service for local validation.
- Configured the GitHub Actions workflow to use a containerized SonarQube scanner against a local service.
- Kept SonarQube properties generic so they are compatible with both local and remote SonarQube instances.

## Key Automation Outcomes

### Repeatable CI/CD Pipeline

A complete Jenkins pipeline is available that executes the full delivery flow from source checkout to Kubernetes deployment. This provides a repeatable, auditable build process that can be extended for production workloads.

### Verified Application Behavior

Automated Pytest validation ensures that application behavior is verified for each change. This prevents regressions for critical APIs such as booking creation and health checks.

### Container-based Delivery

The Docker build stage ensures that the application is packaged consistently across all environments. The image is built once and can be pushed to a registry for reuse in Kubernetes deployment.

### Multi-strategy Kubernetes Deployment

The project includes ready-to-run manifests for advanced deployment techniques:

- Rolling update for zero-downtime version rollout
- Blue-green for instant cutover with fallback
- Canary for controlled release to a small audience
- A/B testing for parallel variant comparison

### Local and Cloud-ready Workflow

Local development is supported with Docker Compose, while cluster deployment is supported with Kubernetes manifests and Minikube bootstrap automation. This dual approach helps maintain development speed while preserving production deployment practices.

## Conclusion

The ACEest Fitness DevOps project provides a practical implementation of modern delivery practices. By combining source control, automated testing, static analysis, containerization, and Kubernetes deployment, the solution demonstrates how a small fitness application can be managed with industry-standard DevOps tooling.

The artifacts created in the repository—including `Jenkinsfile`, `Dockerfile`, `sonar-project.properties`, test suites, and Kubernetes strategy manifests—form a cohesive package for evaluating CI/CD proficiency, release automation, and deployment resilience.
