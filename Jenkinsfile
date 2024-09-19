pipeline {
    agent any
    
    environment {
        VENV_DIR = 'venv'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Virtual Environment') {
            steps {
                sh 'python3 -m venv ${VENV_DIR}'
            }
        }
        
        stage('Upgrade pip') {
            steps {
                sh '. ${VENV_DIR}/bin/activate && python3 -m pip install --upgrade pip'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '. ${VENV_DIR}/bin/activate && pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '. ${VENV_DIR}/bin/activate && pip install pytest'
                sh '. ${VENV_DIR}/bin/activate && python3 -m pytest tests/'
            }
        }
        
        stage('Deploy to Test Environment') {
            steps {
                sh '. ${VENV_DIR}/bin/activate && python3 app.py &'
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
            sh 'pkill -f "python3 app.py" || true'
        }
    }
}