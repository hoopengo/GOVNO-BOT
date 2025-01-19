from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy import select

from bot.db import MessageCapModel, session
from bot.services.mcap_editor import generate_mcap_message

admin_router = Router()


@admin_router.message(Command("mcap", ignore_case=True, ignore_mention=True))
async def _command_mcap_handler(message: Message):
    async with session() as s:
        message_text = await generate_mcap_message()
        message_reply = await message.answer(message_text)

        # Check if a message cap already exists for the chat_id
        result = await s.execute(select(MessageCapModel).where(MessageCapModel.chat_id == message_reply.chat.id))
        existing_cap = result.scalars().first()

        if existing_cap:
            # Update the existing message cap's message_id
            existing_cap.id = message_reply.message_id
        else:
            # Create a new message cap entry
            cap_message = MessageCapModel(message_id=message_reply.message_id, chat_id=message_reply.chat.id)
            s.add(cap_message)

        await s.commit()
