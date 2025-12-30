from plutus import settings


async def message_handler(event):
    # Get details about the chat and the sender
    chat = await event.get_chat()
    sender = await event.get_sender()

    # Handle cases where chat or sender might not have a title/username
    chat_title = chat.title if hasattr(chat, "title") else "Private Chat"
    username = sender.username if sender and hasattr(sender, "username") else "Unknown"

    # You can access settings.CONFIG here if needed in the future
    # e.g., allowed_channels = settings.CONFIG.get('telegram', {}).get('channels', [])

    # Print the message to the console
    # TODO: filter
    # TODO: save to DB
    print(f"[{chat_title}] @{username}")
    print(event.text)
