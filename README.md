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


### 4. Quick Start

Grant Privileges to plutus

```bash
docker container exec -it plutus_db bash

mysql -u root -p
# password: rootpassword
```

```sql
-- before mysql 8.0
GRANT SELECT, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'plutus' IDENTIFIED BY 'plutus';
FLUSH PRIVILEGES;

-- after mysql 8.0
GRANT SELECT, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'plutus'@'%';
FLUSH PRIVILEGES;
```

Flink

```bash
docker container exec -it jobmanager bash

./bin/sql-client.sh
```

```sql
-- 1. Enable Checkpointing (CRITICAL for Iceberg commits)
set 'execution.checkpointing.interval'
= '3s'
;

show databases
;

CREATE TABLE messages (
    id int,
    chat_id int,
    chat_title string,
    sender_id string,
    sender_username string,
    text string,
    `timestamp` TIMESTAMP(0),
    PRIMARY KEY (id) NOT ENFORCED
) WITH (
    'connector' = 'mysql-cdc',
    'hostname' = 'plutus_db',
    'port' = '3306',
    'username' = 'plutus',
    'password' = 'plutus',
    'database-name' = 'plutus',
    'table-name' = 'messages'
);

select *
from messages
;
```
