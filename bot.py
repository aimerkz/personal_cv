import streamlit as st

from aiogram import Bot
from aiogram.exceptions import TelegramAPIError
from envparse import env


env.read_envfile()

TELEGRAM_TOKEN = env.str('TELEGRAM_TOKEN')
CHAT_ID = env.str('CHAT_ID')

bot = Bot(token=TELEGRAM_TOKEN)


async def send_message(message: str):
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
        return True
    except TelegramAPIError as e:
        st.error(f'Error sending message: {e}')
        return False
