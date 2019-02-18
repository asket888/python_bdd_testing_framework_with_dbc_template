/**
 * Run automated ui tests on DEV/UAT enviroment
 */
pipeline {
  agent {
    label 'python3.6-chrome-slave'
  }

  options {
    disableConcurrentBuilds()
    buildDiscarder(logRotator(numToKeepStr:'10'))
    timeout(time: 45, unit: 'MINUTES')
  }

  stages {
    stage('Install deps'){
      steps {
        sh 'pip3 install pipenv'
        sh 'pipenv install --dev --system --deploy'
      }
    }

    stage('Run suite') {
      steps {
        withCredentials([file(credentialsId: 'TEMPLATE_TESTS_CONFIG', variable: 'config_file')]) {
          sh 'ln -s \$config_file ./config.json'
          sh 'invoke run-with-allure --browser=CH_HL --env=${ENV} --tags=${TAGS}'
        }
      }

      post {
        always {
          archiveArtifacts artifacts: '**/artifacts/*'
          allure includeProperties: false,
                 jdk: '',
                 results: [[path: 'artifacts']]
        }
      }
    }
  }

  post {
    success {
      slackSend (channel: '#jenkins', color: '#00FF00', message: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
    }

    failure {
      slackSend (color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
    }

    always {
      cleanWs()
    }
  }
}
