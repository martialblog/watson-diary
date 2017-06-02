# Fake APIs

Provides some API with user data.

## Available APIs

    - Twytta - Twitter like API
    - InstaPic - Instagram like API
    - Friendface - Facebook like API
    - Mail - Gmail like API
    - SMS - Standard SMS Messages

# Usage

It's best to start the API via Docker (docker-compose)

```bash
docker-compose up
```

Building the Docker image:

```bash
docker build -t watson-fakeapi .
```

Running the Container (on localhost port 3000):

```bash
docker run -d -p 3000:3000 watson-fakeapi
```
