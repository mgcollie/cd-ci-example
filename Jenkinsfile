node()
{
    stage('Checkout SCM') {
        checkout scm
    }

    stage('Hello') {
        sh 'echo hello world, I just farted!'
    }

    stage ('Install_Requirements') {
        sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
        sh 'python2.7 get-pip.py'
        sh 'python2.7 -m pip install virtualenv'
        sh 'virtualenv --python=python2.7 venv'
        sh """
            . venv bin activate'
            pip install -r requirements.txt
            make clean
        """
    }
}