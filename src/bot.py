import streamlit as st
import telebot

TELEGRAM_TOKEN = st.secrets["TELEGRAM_TOKEN"]
CHAT_ID = st.secrets["CHAT_ID"]

bot = telebot.TeleBot(TELEGRAM_TOKEN)


def send_message(message: str):
    try:
        bot.send_message(chat_id=CHAT_ID, text=message)
    except telebot.apihelper.ApiException as e:
        st.error(f"Error sending message: {e}")
    else:
        st.success("Message sent!")
