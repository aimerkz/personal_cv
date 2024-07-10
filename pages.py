import streamlit as st

from config import *
from utils import get_hard_skills, get_cv_info, get_work_history, get_contacts_info


def get_about_page():
    st.image(profile_pic, width=350)
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(f'{AGE} years old')
    st.write('Full time work, 100% remote')
    st.download_button(
        label=':page_facing_up: Download resume',
        data=resume,
        file_name=resume_file.name,
        mime='application/octet_stream',
    )
    get_hard_skills()
    get_cv_info()


def get_work_history_page():
    st.title('Work History')
    get_work_history()


def get_contacts_page():
    st.title('Contacts')
    get_contacts_info()


def get_pages():
    page = st.navigation(
        pages=[
            st.Page(get_about_page, title='About me'),
            st.Page(get_work_history_page, title='Work History', url_path='work_history/'),
            st.Page(get_contacts_page, title='Contacts', url_path='contacts/'),
        ],
        position='sidebar',
    )
    return page.run()
