pipeline {
    agent any

    environment {
        VENV_NAME = 'venv'
    }

    stages {
        stage('Check Python Version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh ". ${VENV_NAME}/bin/activate && pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                sh ". ${VENV_NAME}/bin/activate && pytest tests/"
            }
        }

        stage('Deploy to Test Environment') {
            steps {
                sh ". ${VENV_NAME}/bin/activate && python app.py &"
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
            sh 'pkill -f "python app.py" || true'
            sh "rm -rf ${VENV_NAME}"
        }
    }
}