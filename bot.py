import streamlit as st
import telegram


TELEGRAM_TOKEN = st.secrets['TELEGRAM_TOKEN']
CHAT_ID = st.secrets['CHAT_ID']

bot = telegram.Bot(token=TELEGRAM_TOKEN)


async def send_message(message: str):
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
    except telegram.error.TelegramError as e:
        st.error(f'Error sending message: {e}')
    else:
        st.success('Message sent!')
