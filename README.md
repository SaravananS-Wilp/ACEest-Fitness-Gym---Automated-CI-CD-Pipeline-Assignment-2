# ACEest Fitness Gym – Automated CI/CD Pipeline

## Project Overview

This project demonstrates a DevOps-based automated CI/CD pipeline for a simple Fitness Gym web application built using Flask.

The objective of this project is to showcase how modern DevOps tools automate the build, test, and deployment processes.

The pipeline integrates:

* GitHub for version control
* Jenkins for build automation
* Pytest for automated testing
* Docker for containerization

This ensures that every code change is automatically tested and validated before deployment.

---

## Technologies Used

| Technology     | Purpose                    |
| -------------- | -------------------------- |
| Python         | Backend programming        |
| Flask          | Web framework              |
| Pytest         | Unit testing               |
| Docker         | Containerization           |
| Docker Compose | Multi-container management |
| GitHub         | Version control            |
| Jenkins        | CI/CD automation           |

---

## Project Structure

```
ACEest-Fitness-Gym---Automated-CI-CD-Pipeline
│
├── app.py
├── fitness_logic.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
│
├── tests
│   ├── test_fitness_logic.py
|
├── templates
│   ├── index.html
│
├── screenshots
│   └── App Screenshot
│       ├── App Home Page.png
│       ├── BMI - Normal.png
│       ├── BMI - Overweight.png
│       ├── Validation 1 - Weight Negative Value.png
│       ├── Validation 2 - Height Zero Value.png
│   └── Jenkins Screenshot
│       ├── Jenkins Dashboard.png
│       ├── Jenkins Build Configuration.png
│       ├── Jenkins Console Output.png
│
│
└── .github
    └── workflows
        └── main.yml
```

---

## Application Description

The Fitness Gym application calculates basic fitness metrics such as BMI.

### Main Components

**app.py**

Flask application responsible for handling web requests and responses.

**fitness_logic.py**

Contains the core logic for performing fitness calculations, separated from the main application to maintain modularity.

**tests/test_fitness_logic.py**

Unit tests written using Pytest to verify that the fitness logic functions correctly.

---

## User Interface (UI)

A simple web-based user interface has been implemented using Flask templates.

### Features:
- Input fields for weight (kg) and height (m)
- BMI calculation on form submission
- Displays calculated BMI result dynamically

### How it works:
- User enters weight and height
- Form sends POST request to Flask backend
- Backend calculates BMI using `fitness_logic.py`
- Result is displayed on the same page

---

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/SaravananS-Wilp/ACEest-Fitness-Gym---Automated-CI-CD-Pipeline.git
cd ACEest-Fitness-Gym---Automated-CI-CD-Pipeline
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Run the Application

```
python app.py
```

The application will run at:

```
http://localhost:5000
```

---

## Running Unit Tests

Execute the following command:

```
pytest
```

Expected output:

```
9 passed
```

This confirms that the application logic is functioning correctly.

---
## Test Coverage

The project includes a comprehensive Pytest test suite to validate core logic.

#### Test Cases Covered:
- Valid BMI calculation
- Multiple input combinations using parameterized tests
- Zero height (error handling)
- Negative weight and height (validation checks)
- Edge cases for input validation

#### Example Test Cases:
```python
@pytest.mark.parametrize("weight,height,expected", [
    (60, 1.70, 20.76),
    (80, 1.80, 24.69),
    (90, 1.60, 35.16),
])
```
---
## Docker Containerization

Docker ensures that the application runs consistently across different environments.

### Build Docker Image

```
docker build -t fitness-app .
```

### Run Docker Container

```
docker run -p 5000:5000 fitness-app
```

Now access the application at:

```
http://localhost:5000
```

---

## CI/CD Pipeline Workflow

The automated workflow follows this sequence:

```
Developer pushes code
        ↓
GitHub Repository
        ↓
Jenkins CI Pipeline
        ↓
Install Dependencies
        ↓
Run Pytest Unit Tests
        ↓
Build Docker Image
        ↓
Run Docker Container
```

This ensures every code update is automatically tested and validated.

---

## Jenkins Pipeline Steps

Jenkins automates the following steps:

1. Pull code from GitHub repository
2. Install project dependencies
3. Run automated tests using Pytest
4. Build Docker image
5. Deploy and run the container

If all steps execute successfully, Jenkins marks the build as **SUCCESS**.

---

## Screenshots

Refer to the [Screenshots](screenshots/) folder for Jenkins pipeline configuration, build execution screenshots and application UI screen.

---

## Learning Outcomes

Through this project, the following DevOps concepts were implemented:

* Source code management using GitHub
* Automated testing with Pytest
* Containerization using Docker
* Continuous Integration using Jenkins
* CI/CD pipeline design and implementation

---

## Future Improvements

Possible enhancements include:

* Deploying the container to a cloud platform
* Adding Kubernetes orchestration
* Implementing automated production deployment
* Adding monitoring and logging tools
