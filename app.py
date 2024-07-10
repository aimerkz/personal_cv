import streamlit as st

from config import *
from pages import get_pages


# Set general config
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout='centered',
    initial_sidebar_state='expanded',
)

# Load static
with open(css_dir) as css_file:
    css_text = css_file.read()
st.markdown(f'<style>{css_text}</style>', unsafe_allow_html=True)


get_pages()
