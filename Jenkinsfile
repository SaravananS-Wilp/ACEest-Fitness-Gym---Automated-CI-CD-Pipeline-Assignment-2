pipeline {
  agent any
  environment {
    APP_NAME = 'aceest-fitness'
    DOCKER_REGISTRY = 'docker.io'
    IMAGE_NAME = "${DOCKER_REGISTRY}/your-dockerhub-username/${APP_NAME}"
    SONAR_PROJECT_KEY = 'ACEestFitness'
    SONAR_HOST_URL = 'http://sonarqube:9000'
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Prepare') {
      steps {
        sh 'python --version'
        sh 'python -m pip install --upgrade pip'
        sh 'python -m pip install -r requirements.txt'
      }
    }
    stage('Unit Tests') {
      steps {
        sh 'mkdir -p tests/reports'
        sh 'pytest --junitxml=tests/reports/test-results.xml'
      }
    }
    stage('Static Analysis') {
      steps {
        sh "sonar-scanner -Dsonar.projectKey=${SONAR_PROJECT_KEY} -Dsonar.sources=. -Dsonar.host.url=${SONAR_HOST_URL}"
      }
    }
    stage('Build Docker Image') {
      steps {
        sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
      }
    }
    stage('Push Docker Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
          sh 'echo "$DOCKERHUB_PASSWORD" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin ${DOCKER_REGISTRY}'
          sh "docker push ${IMAGE_NAME}:${BUILD_NUMBER}"
        }
      }
    }
    stage('Deploy to Kubernetes') {
      steps {
        sh 'kubectl apply -f k8s/service.yaml'
        sh 'kubectl apply -f k8s/deployment.yaml'
      }
    }
  }
  post {
    always {
      junit 'tests/reports/test-results.xml'
      cleanWs()
    }
    success {
      echo 'Pipeline completed successfully.'
    }
    failure {
      echo 'Pipeline failed. Review the logs in Jenkins.'
    }
  }
}
