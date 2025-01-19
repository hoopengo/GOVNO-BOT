import asyncio

from aiogram import Bot
from aiohttp import ClientSession
from sqlalchemy import select

from bot.db import MessageCapModel, session


async def generate_mcap_message():
    url = "https://api.geckoterminal.com/api/v2/networks/ton/tokens/EQBlWgKnh_qbFYTXfKgGAQPxkxFsArDOSr9nlARSzydpNPwA"
    async with ClientSession() as session:
        response = await session.get(url)
        data = await response.json()
        price_usd = data["data"]["attributes"]["price_usd"]

    return f"""$GOVNO={price_usd}$"""


async def update_mcap_loop(bot: Bot, seconds: int = 15):
    while True:
        cap_text = await generate_mcap_message()

        async with session() as s:
            result = await s.execute(select(MessageCapModel))
            existing_cap = result.scalars().all()

            for cap in existing_cap:
                try:
                    await bot.edit_message_text(cap_text, chat_id=cap.chat_id, message_id=cap.id)
                except Exception:
                    pass

        await asyncio.sleep(seconds)
