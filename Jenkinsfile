pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SUDARSHANJADHAV2/jenkins-docker-flask.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building the Docker image...'
                sh 'docker build -t sudarshansantajijadhav/myapp:latest .'
            }
        }
    }
}
