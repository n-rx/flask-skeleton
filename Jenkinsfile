pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'Github', url: 'https://github.com/n-rx/flask-skeleton.git']]])
            }
        }
        stage('Build'){
            steps {
                git credentialsId: 'Github', url: 'https://github.com/n-rx/flask-skeleton.git'
                sh 'python3 main.py'

            }
        }
        stage("Test"){
            steps {
                echo 'the job been tested'
            }
        }
    }

}
