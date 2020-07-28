pipeline {
 
    agent any

    stages {
        stage("build") {
            steps {
                sh "pip install -r requirements.txt"
            }
        }

        stage("Unit test") {
            steps {
                sh "python test_calculator.py"
            }
        }
    }

}