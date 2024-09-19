pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                sh 'pip install pytest'
                sh 'python -m pytest tests/'
            }
        }
        
        stage('Deploy to Test') {
            steps {
                sh 'python app.py &'  // Start the application in the background
                sh 'echo "Application deployed to test environment"'
            }
        }
    }
    
    post {
        always {
            sh 'pkill -f "python app.py" || true'  // Stop the application
        }
    }
}