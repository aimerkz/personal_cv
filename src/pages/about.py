from typing import TYPE_CHECKING

import streamlit as st

from src.config import PROFILE_IMAGE
from src.utils import display_ed, get_hard_skills

if TYPE_CHECKING:
    from src.types import translate as _


def about_page() -> None:
    col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
    with col1:
        st.image(PROFILE_IMAGE)

    with col2:
        st.title(_("Artem Merkulov"), anchor=False)
        st.write(_("Python Backend Developer"))
        st.write(_("Full time work, 100% remotely"))

    get_hard_skills()
    display_ed()


about_page()
