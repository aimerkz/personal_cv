import streamlit as st

from src.utils import display_projects


def project_page() -> None:
    st.title("My projects")
    display_projects()


project_page()
