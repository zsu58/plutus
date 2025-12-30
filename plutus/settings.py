import os
import yaml
from dotenv import load_dotenv


# Define base directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Load Telegram Credentials
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")

#  Load YAML Config
CONFIG_PATH = os.path.join(BASE_DIR, "config.yaml")
if not os.path.exists(CONFIG_PATH):
    CONFIG = {}
else:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        CONFIG = yaml.safe_load(f)
