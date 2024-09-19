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
                // Use pip3 instead of pip
                sh 'pip3 install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                // Install pytest using pip3
                sh 'pip3 install pytest'
                // Run tests
                sh 'python3 -m pytest tests/'
            }
        }
        
        stage('Deploy to Test') {
            steps {
                // Start the application in the background
                sh 'python3 app.py &'
                sh 'echo "Application deployed to test environment"'
            }
        }
    }
    
    post {
        always {
            // Stop the application after the pipeline finishes
            sh 'pkill -f "python3 app.py" || true'
        }
    }
}
