pipeline {
    agent any

    environment {
        VENV_NAME = 'venv'
        PYTHON_CMD = sh(script: 'which python3 || which python', returnStdout: true).trim()
    }

    stages {
        stage('Check Python Version') {
            steps {
                sh '${PYTHON_CMD} --version'
                sh '${PYTHON_CMD} -m pip --version'
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '${PYTHON_CMD} -m venv ${VENV_NAME}'
                sh ". ${VENV_NAME}/bin/activate && ${PYTHON_CMD} -m pip install --upgrade pip"
            }
        }

        stage('Install Dependencies') {
            steps {
                sh ". ${VENV_NAME}/bin/activate && ${PYTHON_CMD} -m pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                sh ". ${VENV_NAME}/bin/activate && ${PYTHON_CMD} -m pytest tests/"
            }
        }

        stage('Deploy to Test Environment') {
            steps {
                sh ". ${VENV_NAME}/bin/activate && ${PYTHON_CMD} applications/app.py &"
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
            sh 'pkill -f "python applications/app.py" || true'
            sh "rm -rf ${VENV_NAME}"
        }
    }
}