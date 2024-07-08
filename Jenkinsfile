pipeline {
    agent any
    environment {
        SSH_CREDENTIALS = 'your-ssh-credentials-id'
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/springdom/simple_blog.git'
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
                    sshagent([SSH_CREDENTIALS]) {
                        sh '''
                        ssh -o StrictHostKeyChecking=no mtaylor@192.168.1.72 "
                            cd /home/mtaylor/simple_blog &&
                            git reset --hard &&
                            git clean -fd &&
                            git pull origin main &&
                            sudo systemctl restart simpleblog
                        "
                        ssh -o StrictHostKeyChecking=no mtaylor@192.168.1.101 "
                            cd /home/mtaylor/simple_blog &&
                            git reset --hard &&
                            git clean -fd &&
                            git pull origin main &&
                            sudo systemctl restart simpleblog
                        "
                        '''
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Deployment finished.'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
