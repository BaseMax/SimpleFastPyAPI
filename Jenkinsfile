pipeline {
    agent { label 'agent-1' }

    stages {
        stage('Build') {
            steps {
              sh """
                pipenv --python /usr/bin/python3 install
              """
            }
        }
        stage('Dev Deploy') {
            steps {
              sh """
                pipenv run uvicorn main:app --reload&
              """
            }
        }
        stage('Test') {
            steps {
              sh """
                pipenv run pytest tests
              """
            }
        }
    }
}
