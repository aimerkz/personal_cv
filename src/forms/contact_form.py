import re

import streamlit as st


def validate_phone(phone):
    if not re.match(r"^\+?[0-9]+$", phone):
        st.error("Incorrect number format.", icon="💬")
        st.stop()


def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        telegram_login = st.text_input("Telegram Login")
        phone = st.text_input("Phone Number")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not name:
                st.error("Please provide your name.", icon="🧑")
                st.stop()

            if not telegram_login and not phone:
                st.error(
                    "Please provide your phone number or telegram login.", icon="📨"
                )
                st.stop()

            if not message:
                st.error("Please provide a message.", icon="💬")
                st.stop()

            if phone:
                validate_phone(phone)

            message_data = f"Message from {name} - {telegram_login or phone}: {message}"
            st.session_state["message_data"] = message_data
            st.rerun()
