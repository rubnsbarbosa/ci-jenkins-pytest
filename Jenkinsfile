pipeline {
    agent { docker { image 'python:3.8.5' } }
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