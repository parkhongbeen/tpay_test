FROM        python:3.7.5

RUN         python -m pip install --upgrade pip && apt-get -y update && apt-get -y dist-upgrade

COPY        ./requirements.txt /tmp/
RUN         pip install -r /tmp/requirements.txt

COPY        . /srv/tpay_test
WORKDIR     /srv/tpay_test/app

CMD         python manage.py runserver 0.0.0.0:8000
EXPOSE      8000
