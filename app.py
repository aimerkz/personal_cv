import streamlit as st

from config import *
from enums import SectionEnum
from utils import get_contacts_info, get_cv_info, get_hard_skills, get_work_history


st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout='centered',
    initial_sidebar_state='expanded',
)

# Load static
with open(css_dir) as css_file:
    st.markdown(
        '<style>{}</style>'.format(css_file.read()),
        unsafe_allow_html=True,
    )

# Create navigation
navigation = st.sidebar.radio(
    'Navigation',
    ('About me', 'Work history', 'Contacts')
)


match navigation:
    case SectionEnum.ABOUT.value:
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

    case SectionEnum.WORK_HISTORY.value:
        st.title("Work History")
        get_work_history()

    case SectionEnum.CONTACTS.value:
        st.title("Contacts")
        get_contacts_info()
