import re

import streamlit as st


def validate_phone(phone: str) -> None:
    if not re.match(r"^\+?[0-9]+$", phone):
        st.error("Incorrect number format.", icon="💬")
        st.stop()


def contact_form():
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("First Name")
        telegram_login = st.text_input("Telegram Login")
        phone = st.text_input("Phone Number")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button(
            label="Submit", help="Click to send message"
        )

        if submit_button:
            if name is None:
                st.error("Please provide your name.", icon="🧑")
                st.stop()

            if telegram_login is None and phone is None:
                st.error(
                    "Please provide your phone number or telegram login.", icon="📨"
                )
                st.stop()

            if message is None:
                st.error("Please provide a message.", icon="💬")
                st.stop()

            if phone is not None:
                validate_phone(phone)

            message_data = f"Message from {name} - {telegram_login or phone}: {message}"
            st.session_state["message_data"] = message_data
            st.rerun()
