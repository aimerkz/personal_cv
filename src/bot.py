from typing import TYPE_CHECKING

import streamlit as st
import telebot

if TYPE_CHECKING:
    from src.types import _


@st.cache_resource(ttl=None, show_spinner=False)
def get_tg_bot() -> telebot.TeleBot:
    tg_token = st.secrets["TELEGRAM_TOKEN"]
    return telebot.TeleBot(tg_token)


class TelegramBot:
    def __init__(
        self, bot: telebot.TeleBot | None = None, chat_id: int | None = None
    ) -> None:
        self._bot = bot
        self._chat_id = chat_id

    @property
    def bot(self) -> telebot.TeleBot:
        if self._bot is None:
            self._bot = get_tg_bot()
        return self._bot

    @property
    def chat_id(self) -> int:
        if self._chat_id is None:
            self._chat_id = st.secrets["CHAT_ID"]
        return self._chat_id

    def send_message(self, message: str) -> None:
        try:
            self.bot.send_message(chat_id=self.chat_id, text=message)
        except telebot.apihelper.ApiException:
            st.error(_("Error sending message"))
        else:
            st.success(_("Message sent!"))


tg_bot = TelegramBot()
