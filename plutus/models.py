from sqlalchemy import Column, BigInteger, String, Text, DateTime
from sqlalchemy.sql import func
from plutus.database import Base


class Message(Base):
    __tablename__ = "messages"
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    chat_id = Column(BigInteger, nullable=True)  # This is the Telegram Chat ID
    chat_title = Column(String(255), nullable=True)
    sender_id = Column(BigInteger, nullable=True)
    sender_username = Column(String(255), nullable=True)
    text = Column(Text, nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
