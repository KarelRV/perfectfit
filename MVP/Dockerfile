FROM ubuntu

RUN apt-get update

RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential

RUN apt-get install -y python python-dev python-distribute python-pip

ADD / /login-app

RUN pip install -r /login-app/requirements.txt

WORKDIR /login-app

CMD python application.py