import streamlit as st

from src.utils import display_work_history


def work_history_page() -> None:
    st.title("Work History")
    display_work_history()


work_history_page()
