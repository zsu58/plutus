# Plutus

## Setup

### 1. Prerequisites
- Python 3.10+
- Docker & Docker Compose

### 2. Configuration

1. Create a `.env` file in the root directory:
```
   API_ID=your_api_id
   API_HASH=your_api_hash

   DB_HOST=localhost
   DB_PORT=3306
   DB_USER=plutus_user
   DB_PASSWORD=plutus_password
   DB_NAME=plutus
```

2. Create a python virtual environment and install the dependencies

```bash
pip install -r requirements.txt
```

3. Create a `config.yaml` file in the root directory

4. Build the Docker image

```bash
docker build -f docker/Dockerfile.plutus -t plutus-app .
docker build -f docker/Dockerfile.flink -t flink .
```

### 3. Run

```bash
docker network create \
  --driver bridge \
  data-net
```


```bash
docker-compose -f docker-compose.plutus.yml up

# Client is starting... (Check terminal for login instructions if first time)
# Please enter your phone (or bot token): +821012345678
# Please enter the code you received: {message_code from telegram}

# not working
# docker-compose -f docker-compose.ceph.yml up

docker-compose -f docker-compose.minio.yml up
# create a bucket http://localhost:9000

docker-compose -f docker-compose.flink.yml up
```

* Flink UI: http://localhost:8081/#/overview
* MySQL: http://localhost:3306
* Python App: http://localhost:8000
* Minio: http://localhost:9000