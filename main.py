import os
from dotenv import load_dotenv
from telethon import TelegramClient, events


load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
client = TelegramClient("my_session", API_ID, API_HASH)


@client.on(events.NewMessage)
async def handler(event):
    # Get details about the chat and the sender
    chat = await event.get_chat()
    sender = await event.get_sender()

    # Handle cases where chat or sender might not have a title/username
    chat_title = chat.title if hasattr(chat, "title") else "Private Chat"
    username = sender.username if sender and hasattr(sender, "username") else "Unknown"

    # Print the message to the console
    print(f"[{chat_title}] @{username}")
    print(event.text)


if __name__ == "__main__":
    print("Client is starting... (Check terminal for login instructions if first time)")
    client.start()
    client.run_until_disconnected()
