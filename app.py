import streamlit as st

from utils import get_cv_info, get_hard_skills, get_work_history
from config import *
from enums import SectionEnum


st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout='centered',
    initial_sidebar_state='expanded',
)

st.markdown(
    """
    <style>
    ul {
        list-style-type: none;
        padding-left: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col_1, col_2 = st.columns(2, gap='medium')
with col_1:
    st.image(profile_pic, width=320)

with col_2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(f'{AGE} years old')
    st.download_button(
        label=':page_facing_up: Download resume',
        data=resume,
        file_name=resume_file.name,
        mime='application/octet_stream',
    )

# Настройка боковой панели
st.sidebar.title("Navigation")

# Добавление виджетов на боковую панель
option = st.sidebar.selectbox(
    'Choose a section:',
    ('About me', 'Work history', 'Contacts')
)


match option:
    case SectionEnum.ABOUT.value:
        get_hard_skills()
        get_cv_info()
    case SectionEnum.CONTACTS.value:
        ...
    case SectionEnum.WORK_HISTORY.value:
        get_work_history()
