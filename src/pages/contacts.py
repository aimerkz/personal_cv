from typing import TYPE_CHECKING

import streamlit as st

from src.bot import tg_bot
from src.forms.contact_form import contact_form
from src.utils import get_contacts_info

if TYPE_CHECKING:
    from src.types import translate as _


@st.dialog(_("Contact Me"))
def show_contact_form():
    contact_form()


def contacts_page() -> None:
    st.title(_("Contacts"))
    get_contacts_info()

    st.subheader(_("Also you can write to my bot in Telegram:"))

    if st.button(
        label=_("Send"),
        key="send",
        help=_("Open form to send messages"),
    ):
        show_contact_form()

    if "message_data" in st.session_state:
        message = st.session_state.pop("message_data")
        tg_bot.send_message(message)


contacts_page()
