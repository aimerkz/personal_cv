import streamlit as st

from src.utils import display_projects

import gettext

_ = gettext.gettext


def project_page() -> None:
    st.title(_("My projects"))
    display_projects()


project_page()
