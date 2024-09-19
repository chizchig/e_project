pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "rise-app:${env.BUILD_ID}"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }
        stage('Run Tests') {
            steps {
                sh "docker run --rm ${DOCKER_IMAGE} /venv/bin/pytest tests/"
            }
        }
        stage('Deploy to Test Environment') {
            steps {
                sh "docker run -d --name rise-app-test -p 5000:5000 ${DOCKER_IMAGE}"
                sh 'echo "Application deployed to test environment"'
                sh 'sleep 5' // Give the app a moment to start up
            }
        }
        stage('Verify Deployment') {
            steps {
                sh 'curl http://localhost:5000 || exit 1'
            }
        }
    }
    post {
        always {
            sh 'docker stop rise-app-test || true'
            sh 'docker rm rise-app-test || true'
            sh "docker rmi ${DOCKER_IMAGE} || true"
        }
    }
}