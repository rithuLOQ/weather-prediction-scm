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
                sh 'pip install -r requirements.txt'
                sh 'pip install pytest'
                
                // Running Sanjana and Sahaana's SCM Configuration Items
                sh 'pytest test_regression.py'
                sh 'pytest test_classification.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t weather-app:latest .'
            }
        }
    }
}