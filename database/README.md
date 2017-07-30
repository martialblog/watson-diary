# Database

## Setup

```bash
docker run -p 27017:27017 -d --name watson-mongodb mongo
docker exec -it watson-mongodb /bin/bash

# Open Mongo Shell

db.createCollection("users")
db.createCollection("feeds")
db.createCollection("reports")
```
