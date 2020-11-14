FROM nginx:1.15

RUN apt-get update
RUN apt-get install -y curl gnupg2 apt-transport-https nodejs git yarn build-essentials

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update
RUN curl -sL https://deb.nodesource.com/setup_15.x | bash -

WORKDIR /app
ADD package.json /app/package.json
ADD yarn.lock /app/yarn.lock

RUN yarn install

ADD . /app

RUN make build

COPY nginx.conf /etc/nginx/conf.d/default.conf

CMD ["make", "run"]
