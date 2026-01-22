import os
import yaml
from dotenv import load_dotenv


# Define base directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Load Telegram Credentials
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")

# Database Configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER", "plutus_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "plutus_password")
DB_NAME = os.getenv("DB_NAME", "plutus")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

#  Load YAML Config
CONFIG_PATH = os.path.join(BASE_DIR, "config.yaml")
if not os.path.exists(CONFIG_PATH):
    CONFIG = {}
else:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        CONFIG = yaml.safe_load(f)
