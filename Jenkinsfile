pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Environment') {
            steps {
                echo 'Starting Lab 021 Jenkins Pipeline'
                sh 'whoami'
                sh 'pwd'
                sh 'python3 --version'
            }
        }

        stage('Build') {
            steps {
                echo 'Checking application'
                sh 'python3 src/app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests'
                sh 'python3 -m unittest discover -s tests -v'
            }
        }

        stage('Package') {
            steps {
                echo 'Creating build artifact'
                sh '''
                    mkdir -p dist
                    tar -czf dist/lab-021-application.tar.gz \
                        src tests README.md
                    ls -lh dist/
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }

        failure {
            echo 'Pipeline failed. Review the console output.'
        }

        always {
            echo 'Pipeline execution finished'
        }
    }
}
