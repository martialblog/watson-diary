FROM node:alpine as builder
LABEL maintainer="markus.opolka@fau.de"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN npm install
RUN npm run build

FROM nginx:alpine
LABEL maintainer="markus.opolka@fau.de"

WORKDIR /usr/share/nginx/html/
COPY --from=builder /usr/src/app .

EXPOSE 80