pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run SCM Automated Tests') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'pip install pytest'
                
                // Running Sanjana and Sahaana's SCM Configuration Items
                bat 'python -m pytest test_regression.py'
                bat 'python -m pytest test_classification.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t weather-app:latest .'
            }
        }
    }
}