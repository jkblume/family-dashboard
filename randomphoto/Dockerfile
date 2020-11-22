FROM python:3.7

WORKDIR /app

ADD requirements.txt requirements.txt 
RUN pip install -r requirements.txt

ADD . /app

CMD make run
