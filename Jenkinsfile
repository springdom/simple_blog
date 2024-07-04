pipeline {
    agent any

    environment {
        SSH_CREDENTIALS = '1543ab92-7e92-4428-9ca2-407e49c80cb2'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/springdom/simple_blog.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    def servers = ['192.168.1.72', '192.168.1.101']
                    withCredentials([sshUserPrivateKey(credentialsId: env.SSH_CREDENTIALS, keyFileVariable: 'SSH_KEY')]) {
                        servers.each { server ->
                            sh """
                            ssh -i ${SSH_KEY} mtaylor@${server} << 'EOF'
                                cd /home/mtaylor/simple_blog
                                git pull
                                sudo systemctl restart simpleblog
                            EOF
                            """
                        }
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment completed successfully!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}