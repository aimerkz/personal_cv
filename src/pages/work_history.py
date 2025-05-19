import streamlit as st

from src.utils import display_work_history

import gettext

_ = gettext.gettext


def work_history_page() -> None:
    st.title(_("Work History"))
    display_work_history()


work_history_page()
