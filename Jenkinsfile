pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t student-feedback-app .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker stop feedback || exit 0'
                bat 'docker rm feedback || exit 0'
                bat 'docker run -d -p 5000:5000 --name feedback student-feedback-app'
            }
        }
    }
}