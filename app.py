import streamlit as st

from config import CSS_DIR


# Pages setup
about_page = st.Page(
    'views/about.py',
    title='About Me',
    icon='☕',
    default=True,
)
work_history_page = st.Page(
    'views/work_history.py',
    title='Work history',
    icon='🧑‍💼',
)
contacts_page = st.Page(
    'views/contacts.py',
    title='Contacts',
    icon='📒',
)


# Pages navigation
pg = st.navigation(
    {
        'Home': [about_page],
        'Info': [work_history_page, contacts_page],
    }
)

st.sidebar.text('🍀 by Artem Merkulov')

# Load static
with open(CSS_DIR) as css_file:
    css_text = css_file.read()
st.markdown(f'<style>{css_text}</style>', unsafe_allow_html=True)

pg.run()
