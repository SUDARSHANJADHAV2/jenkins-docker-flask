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
        stage('Run Container') {
            steps {
                echo 'Starting the container...'
                sh 'docker rm -f my_flask_app || true'
                
                sh 'docker run -d -p 5050:5000 --name my_flask_app sudarshansantajijadhav/myapp:latest'
            }
        }
        stage('Verify Container') {
            steps {
                echo 'Verifying the container is running...'
                sh 'docker ps -f name=my_flask_app'
            }
        }
    }
}
