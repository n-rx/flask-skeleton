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
                script {
                    try {
                        sh 'sudo rm -r /opt/nrx/flask_skeleton'
                    }
                    catch (Exception e){
                        echo "rm error. Dir not exist"
                    }
                }
                script {
                    try {
                        sh 'sudo mkdir /opt/nrx/flask_skeleton'
                    }
                    catch (Exception e){
                        echo "mkdir error. dir exist"
                    }
                }
                git credentialsId: 'Github', url: 'https://github.com/n-rx/flask-skeleton.git'
                sh 'sudo cp -r . /opt/nrx/flask_skeleton'
            }
        }

        stage("Docker build"){
            steps{
                sh 'sudo docker compose -f /opt/nrx/docker-compose.yml build'
            }
        }

        stage("Docker start"){
            steps{
                echo "Try to stop previous version"
                script{
                    try{
                        sh 'sudo docker compose -f /opt/nrx/docker-compose.yml stop'
                    }
                    catch (Exception e){
                        echo 'not running'
                    }
                }
                sh 'sudo docker compose -f /opt/nrx/docker-compose.yml up -d'
            }
        }

        stage("Test"){
            steps {
                sh "curl http://127.0.0.1:8000/api/data"
            }
        }
    }
}