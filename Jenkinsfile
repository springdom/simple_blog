pipeline {
    agent any

    environment {
        SSH_CREDENTIALS_ID = '1543ab92-7e92-4428-9ca2-407e49c80cb2'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/springdom/simple_blog.git'
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest tests/
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: "${env.SSH_CREDENTIALS_ID}", keyFileVariable: 'SSH_KEY')]) {
                        def servers = ['192.168.1.72', '192.168.1.101']
                        servers.each { server ->
                            sh """
                            ssh -i ${SSH_KEY} -o StrictHostKeyChecking=no user@${server} 'cd /path/to
