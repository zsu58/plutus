import sys
import argparse

from telethon import TelegramClient, events
from plutus import settings, database, models
from plutus.handlers import message_handler


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plutus Telegram Bot")
    parser.add_argument("--init", action="store_true", help="Initialize the database and authenticate, then exit")
    args = parser.parse_args()
    
    if not args.init:
        print(f"Loaded config for: {list(settings.CONFIG.keys())}")

        # Initialize Database Tables
        models.Base.metadata.create_all(bind=database.engine)
        print("Database initialized.")

        client = TelegramClient("my_session", settings.API_ID, settings.API_HASH)

        # Register the handler manually
        client.add_event_handler(message_handler, events.NewMessage)

        print("Client is starting...")
        client.start()
        client.run_until_disconnected()
    else:
        print("Running in initialization mode...")
        # Authenticate with Telegram
        client = TelegramClient("my_session", settings.API_ID, settings.API_HASH)
        print("Client is starting... (Check terminal for login instructions)")
        # client.start(bot_token=settings.BOT_TOKEN)
        client.start()
        client.run_until_disconnected()
