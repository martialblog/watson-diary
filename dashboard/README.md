# Dr. Watson Frontend

The Dr. Watson Dashboard is a Vue.js Application to communicate with the Backend.

## Usage

### Docker

To build a container:
``` bash
docker build -t watson-dashboard -f Dockerfile .
docker run --name some-nginx -d -p 8080:80 watson-dashboard
```

### Node

To run the Dashboard directly:
``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build
```
