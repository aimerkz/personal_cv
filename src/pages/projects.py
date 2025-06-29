from typing import TYPE_CHECKING

import streamlit as st

from src.utils import display_projects

if TYPE_CHECKING:
    from src.types import translate as _


def project_page() -> None:
    st.title(_("My projects"))
    display_projects()


project_page()
