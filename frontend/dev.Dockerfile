FROM node:latest

WORKDIR /usr/app

RUN npm install node-fetch

ENTRYPOINT ["tail", "-f", "/dev/null"]