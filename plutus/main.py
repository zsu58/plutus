from telethon import TelegramClient, events
from plutus import settings
from plutus.handlers import message_handler


if __name__ == "__main__":
    print(f"Loaded config for: {list(settings.CONFIG.keys())}")

    client = TelegramClient("my_session", settings.API_ID, settings.API_HASH)

    # Register the handler manually
    client.add_event_handler(message_handler, events.NewMessage)

    print("Client is starting... (Check terminal for login instructions if first time)")
    client.start()
    client.run_until_disconnected()
