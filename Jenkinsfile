






pipeline {
    agent any

    options {
        timestamps()
    }

    environment {
        PYTHON = 'C:\\Users\\abina\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    }

    stages {

        stage('Environment') {
            steps {
                echo 'Starting Lab 021 Jenkins Pipeline'

                bat 'java -version'
                bat 'git --version'
                bat '"%PYTHON%" --version'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Python application'

                bat '"%PYTHON%" src\\app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Python unit tests'

                bat '"%PYTHON%" -m unittest discover -s tests -v'
            }
        }

        stage('Package') {
            steps {
                echo 'Creating application package'

                bat 'if not exist dist mkdir dist'

                bat 'tar -czf dist\\lab-021-application.tar.gz src tests README.md'

                archiveArtifacts artifacts: 'dist/*.tar.gz',
                                 fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Lab 021 Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check Console Output.'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}

