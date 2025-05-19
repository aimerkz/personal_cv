import re

import streamlit as st

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.types import _


def validate_phone(phone: str) -> None:
    if not re.match(r"^\+?[0-9]+$", phone):
        st.error(_("Incorrect number format."), icon="💬")
        st.stop()


def contact_form():
    with st.form("contact_form", clear_on_submit=False):
        name = st.text_input(_("First Name"))
        telegram_login = st.text_input(_("Telegram Login"))
        phone = st.text_input(_("Phone Number"))
        message = st.text_area(_("Your Message"))
        submit_button = st.form_submit_button(
            label=_("Submit"), help=_("Click to send message")
        )

        if submit_button:
            if not name:
                st.error(_("Please provide your name."), icon="🧑")
                st.stop()

            if not telegram_login and not phone:
                st.error(
                    _("Please provide your phone number or telegram login."), icon="📨"
                )
                st.stop()

            if not message:
                st.error(_("Please provide a message."), icon="💬")
                st.stop()

            if phone:
                validate_phone(phone)

            message_data = "{} {} - {}: {}".format(
                _("Message from"), name, telegram_login, message
            )
            st.session_state["message_data"] = message_data
            st.rerun()
