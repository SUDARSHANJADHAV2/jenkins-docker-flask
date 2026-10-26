pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SUDARSHANJADHAV2/jenkins-docker-flask.git'
            }
        }
        stage('Display Message') {
            steps {
                echo 'Successfully cloned the repository. Starting build process...'
            }
        }
    }
}
