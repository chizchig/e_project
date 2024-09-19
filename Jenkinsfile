pipeline {
    agent any
    
    environment {
        // Define environment variables if needed
        VENV_DIR = 'venv'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the latest code from the GitHub repository
                checkout scm
            }
        }
        
        stage('Setup Virtual Environment') {
            steps {
                // Create and activate a Python virtual environment
                sh 'python3 -m venv ${VENV_DIR}'
                sh '. ${VENV_DIR}/bin/activate'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Install dependencies using pip
                sh '. ${VENV_DIR}/bin/activate && pip install -r requirements.txt'
            }
        }
        
        stage('Build') {
            steps {
                // Build the application (adjust command if needed)
                sh '. ${VENV_DIR}/bin/activate && python3 setup.py build'
            }
        }
        
        stage('Test') {
            steps {
                // Install pytest if not already included in requirements.txt
                sh '. ${VENV_DIR}/bin/activate && pip install pytest'
                // Run tests using pytest
                sh '. ${VENV_DIR}/bin/activate && python3 -m pytest tests/'
            }
        }
        
        stage('Deploy to Test') {
            steps {
                // Deploy the application to the test environment
                sh '. ${VENV_DIR}/bin/activate && python3 app.py &'
                sh 'echo "Application deployed to test environment"'
            }
        }
    }
    
    post {
        always {
            // Stop the application after the pipeline finishes
            sh 'pkill -f "python3 app.py" || true'
            // Archive the build artifacts (optional)
            archiveArtifacts artifacts: '**/target/*.zip', allowEmptyArchive: true
            // Publish test results (if using JUnit or similar)
            junit '**/test-results/*.xml'
        }
    }
}
