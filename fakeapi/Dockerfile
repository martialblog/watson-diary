FROM node:alpine
LABEL maintainer="markus.opolka@fau.de"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN npm install

EXPOSE 3000
CMD ["npm", "start"]