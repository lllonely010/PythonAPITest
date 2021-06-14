pipeline {
  
  stages {
    stage('TestSuite Run') {
      steps {
        git(url: 'ssh://******.git', credentialsId: '*********')
        // notifyBitbucket()
        container(name: 'testsuite') {
          sh '''
            cd /opt/mypython//workspace && pytest -v --no-summary --html=/workspace/reports/report.html --self-contained-html pythonapi
          '''
        }
      }
    }
  }
}

                