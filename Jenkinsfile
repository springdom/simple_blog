pipeline {
    agent { label 'agent1'}

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', 
                          branches: [[name: '*/main']], 
                          userRemoteConfigs: [[url: 'https://github.com/springdom/simple_blog.git']]
                         ])
            }
        }
        stage('Check for Unstaged Changes') {
            steps {
                script {
                    def status = sh(script: 'git status --porcelain', returnStdout: true).trim()
                    if (status) {
                        error "There are unstaged changes in the repository. Please commit or stash your changes before proceeding."
                    }
                }
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh '''
                rm -rf venv
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
                sh 'echo hello'
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                        def servers = ['192.168.1.72', '192.168.1.101']
                        servers.each { server ->
                            sh """
                            ssh -o StrictHostKeyChecking=no mtaylor@${server} 'cd /home/mtaylor/simple_blog && git pull origin main && sudo systemctl restart simpleblog'
                            """
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Deployment finished.'
        }
        success {
            echo 'Deployment succeeded!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
