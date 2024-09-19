# EmpireHub

EmpireHub is a web application built with Flask, designed for user management and messaging features. This project includes a basic setup with user authentication, chat functionality, and a dashboard. It uses a SQLite database and is configured to run with Jenkins for continuous integration and deployment.

## Project Structure
├── Jenkinsfile ├── README.md ├── app.py ├── instance │ └── site.db ├── requirements.txt ├── static │ └── style.css ├── templates │ ├── activities.html │ ├── base.html │ ├── chat.html │ ├── dashboard.html │ ├── home.html │ └── signup.html └── tests └── test_app.py

## Requirements

- Python 3.6+
- Flask
- Flask-SQLAlchemy
- python-dotenv
- pytest
- SQLAlchemy
- Werkzeug

## Set up a virtual environment:

python3 -m venv venv
source venv/bin/activate

## Installation of Requirements(depependies)
pip install -r requirements.txt

To setup environmental variables, I created .env
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///site.db

## application Test Run 
python app.py
The application will be available at http://localhost:5000.

Access the application:

Home Page: http://localhost:5000/
Sign Up: http://localhost:5000/signup
Login: http://localhost:5000/
Dashboard: http://localhost:5000/dashboard
Activities: http://localhost:5000/activities
Chat: http://localhost:5000/chat

## Jenkins Integration
This project includes a Jenkins pipeline for continuous integration and deployment. The pipeline performs the following steps:

Checkout: Retrieves the latest code from the repository.
Setup Virtual Environment: Creates and activates a Python virtual environment.
Upgrade pip: Upgrades pip to the latest version.
Install Dependencies: Installs the required Python packages.
Run Tests: Executes the test suite using pytest.
Deploy to Test Environment: Starts the Flask application in the test environment.
Verify Deployment: Checks if the application is running correctly.
Jenkinsfile
The Jenkinsfile defines the pipeline stages and steps for the CI/CD process. Ensure Jenkins is configured with appropriate permissions and plugins to use this pipeline.

## Note
It is important to note that the Jenkins_server is hosted in another repository, running on AWS EC2. This application is in a github repository and the webhook(http://host_instance_ip/github-webhook/) alerts of any changes made in the code.
