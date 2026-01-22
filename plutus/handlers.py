from plutus import settings, database, models


async def message_handler(event):
    # Get details about the chat and the sender
    chat = await event.get_chat()
    sender = await event.get_sender()

    # Handle cases where chat or sender might not have a title/username
    chat_title = chat.title if hasattr(chat, "title") else "Private Chat"
    username = sender.username if sender and hasattr(sender, "username") else "Unknown"

    # You can access settings.CONFIG here if needed in the future
    # e.g., allowed_channels = settings.CONFIG.get('telegram', {}).get('channels', [])
    # TODO: filter the messages using CONFIG and renotify the user about the interested stocks

    # Print the message to the console
    print(f"[{chat_title}] @{username}")
    print(event.text)

    # Save to DB
    save_message(chat, chat_title, sender, username, event.text)

    #


def save_message(chat, chat_title, sender, username, text):
    db = database.SessionLocal()
    try:
        new_message = models.Message(
            chat_id=chat.id if chat else None,
            chat_title=chat_title,
            sender_id=sender.id if sender else None,
            sender_username=username,
            text=text,
        )
        db.add(new_message)
        db.commit()
    except Exception as e:
        print(f"Error saving to DB: {e}")
        db.rollback()
    finally:
        db.close()
