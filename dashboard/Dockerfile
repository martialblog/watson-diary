FROM node:alpine as builder
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN npm install
RUN npm run build

FROM nginx:alpine
EXPOSE 80
WORKDIR /usr/share/nginx/html/
COPY --from=builder /usr/src/app .