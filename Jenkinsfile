node()
{
    stage('Checkout SCM') {
        checkout scm
    }

    stage('Hello') {
        sh 'echo hello world, I just farted!'
    }

    stage ('Install_Requirements') {
        sh """
            echo ${SHELL}
            [ -d venv ] && rm -rf venv
            #virtualenv --python=python2.7 venv
            virtualenv venv
            #. venv/bin/activate
            export PATH=${VIRTUAL_ENV}/bin:${PATH}
            pip install --upgrade pip
            pip install -r requirements.txt -r dev-requirements.txt
            make clean
        """
    }
}