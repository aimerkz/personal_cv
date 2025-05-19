import streamlit as st

from src.utils import display_projects

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.types import _


def project_page() -> None:
    st.title(_("My projects"))
    display_projects()


project_page()
