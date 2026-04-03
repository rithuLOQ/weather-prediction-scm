pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                // Build the container first
                bat 'docker build -t weather-app:latest .'
            }
        }
        stage('Run SCM Automated Tests') {
            steps {
                // Run the tests INSIDE the isolated Linux container!
                bat 'docker run --rm weather-app:latest sh -c "pip install pytest && pytest test_regression.py && pytest test_classification.py"'
            }
        }
    }
}