pipeline {
    agent any

    stages {

        stage('Run Tests in Docker') {
            steps {
                sh '''
                docker run --rm \
                -v $(pwd):/app \
                -w /app \
                python:3.10 \
                sh -c "pip install -r requirements.txt && pip install pytest && pytest"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fitness-app .'
            }
        }
    }
}