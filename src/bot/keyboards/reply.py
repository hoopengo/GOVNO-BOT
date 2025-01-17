from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Привет из клавиатуры"),
        ],
    ],
    is_persistent=True,
    resize_keyboard=True,
)
