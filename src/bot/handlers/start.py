from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.reply import menu_kb

start_router = Router()


@start_router.message(CommandStart(ignore_case=True, ignore_mention=True))
async def _command_start_handler(message: Message):
    # send start message
    await message.answer(
        "<b>Приветствую в тестовом боте!</b> 💕",
        reply_markup=menu_kb,
    )
