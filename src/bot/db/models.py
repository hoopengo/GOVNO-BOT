from sqlalchemy import BigInteger, Column

from bot.db.base import Base

# class UserModel(Base):
#     """SQLAlchemy model for a user."""

#     __tablename__ = "user"

#     id = Column(BigInteger, primary_key=True, index=True, nullable=False, unique=True)
#     cap_messages = relationship("MessageCapModel", back_populates="user", cascade="all, delete-orphan")

#     def __init__(self, user_id: int):
#         """Initialize a UserModel instance with a user ID."""
#         self.id = user_id

#     def __repr__(self) -> str:
#         """Return a string representation of the UserModel instance."""
#         return f"<User {self.id}>"


class MessageCapModel(Base):
    """SQLAlchemy model for message caps."""

    __tablename__ = "message_cap"

    id = Column(BigInteger, unique=True, primary_key=True, index=True, nullable=False)
    chat_id = Column(BigInteger, unique=True, nullable=False)

    def __init__(self, message_id: int, chat_id: int):
        self.id = message_id
        self.chat_id = chat_id

    def __repr__(self) -> str:
        """Return a string representation of the MessageCapModel instance."""
        return f"<MessageCap {self.id}>"
