pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t student-feedback-app .'
            }
        }

       stage('Deploy with Ansible') {
    steps {
        bat 'ansible-playbook ansible/deploy.yml'
    }
}
    }
}