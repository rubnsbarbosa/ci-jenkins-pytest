pipeline {
    agent { label 'docker-agent' }
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Unit test') {
            steps {
                sh 'pytest'
            }
        }
    }
}