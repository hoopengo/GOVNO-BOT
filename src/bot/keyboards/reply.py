from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Следить за ценой!", url="t.me/govno_price"),
        ],
    ],
)
