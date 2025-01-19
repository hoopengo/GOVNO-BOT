from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.reply import menu_kb

start_router = Router()


@start_router.message(CommandStart(ignore_case=True, ignore_mention=True))
async def _command_start_handler(message: Message):
    # send start message
    await message.answer(
        """<b>Добро пожаловать в говнобота!</b> 💩
        
Снизу кнопка чтобы перейти на наш канал с обновлением цены $GOVNO каждые 15 секунд!
Также вы можете прописать команду <code>/mcap</code> чтобы следить за ценой здесь или в любом чате где есть бот.
        
<i>Закинуть говна автору:</i> <code>UQByaELlaQ-S-TtKe-B3xWRQGDlSc2Kfn86Cccz2NazxpYmv</code>""",
        reply_markup=menu_kb,
    )
