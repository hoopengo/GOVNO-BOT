from sqlalchemy import Column, Integer

from bot.db.base import Base


class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, unique=True, primary_key=True, index=True, nullable=False)

    def __init__(self, message_id: int):
        self.id = message_id

    def __repr__(self):
        return f"<User {self.id}>"
