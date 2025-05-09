import streamlit as st

from src.config import DESCRIPTION, NAME, load_profile_image
from src.utils import display_ed, get_hard_skills


def about_page() -> None:
    col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
    with col1:
        profile_image = load_profile_image()
        st.image(profile_image, use_container_width=True, width=300)

    with col2:
        st.title(NAME, anchor=False)
        st.write(DESCRIPTION)
        st.write("Full time work, 100% remotely")

    get_hard_skills()
    display_ed()


about_page()
