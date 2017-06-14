# Dr. Watson Backend

This is the backend for the Dr. Watson Application. It provides a Python based RESTful API to communicate with.

# Usage

If you're not using Docker you're required to install a MongoDB instance.

## Python

Install requirements:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

Start the API:

```bash
python3 app.py
```

## Docker

```bash
docker-compose up
```
