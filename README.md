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

### 3. Run

```bash
docker-compose up -d
python -m plutus.main

Client is starting... (Check terminal for login instructions if first time)
Please enter your phone (or bot token): +821012345678
Please enter the code you received: {message_code from telegram}
```