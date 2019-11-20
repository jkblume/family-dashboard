FROM arm32v7/node:lts-slim

RUN apt-get update
RUN apt-get install -y make

ADD . /app
WORKDIR /app

RUN npm install

CMD make run

EXPOSE 8080