# ACEest Fitness Gym - Automated CI/CD Pipeline

## Project Overview
This project demonstrates a DevOps CI/CD pipeline for a Flask-based fitness application. The pipeline automatically tests and builds the application whenever code is pushed to GitHub.

## Technologies Used
- Python
- Flask
- Pytest
- Docker
- GitHub Actions

## Pipeline Workflow
1. Developer pushes code to GitHub
2. GitHub Actions triggers the CI pipeline
3. Dependencies are installed
4. Automated tests are executed using Pytest
5. Docker image is built
6. Docker container is started

## Repository Structure

app.py
fitness_logic.py
requirements.txt
Dockerfile
tests/test_fitness_logic.py
.github/workflows/ci.yml


## Running the Application Locally

Build Docker Image: docker build -t fitness-app .


Run Container: docker run -p 5000:5000 fitness-app


Then open: http://localhost:5000


## CI/CD Automation

The CI pipeline is implemented using GitHub Actions and automatically runs on every push too the 'main' branch