FROM python:3.7

WORKDIR /app

ADD requirements.txt requirements.txt 
RUN pip install -r requirements.txt

ADD . /app

ENV GOOGLE_CLIENT_SECRET_JSON_AS_BASE64=""

CMD make run
