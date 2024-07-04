pipeline {
    agent { label 'agent1' }  // Ensure this label matches the agent's label

    environment {
        SSH_CREDENTIALS = 'your-ssh-credentials-id'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/springdom/simple_blog.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest
                '''
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
                                cd /path/to/simple_blog
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
