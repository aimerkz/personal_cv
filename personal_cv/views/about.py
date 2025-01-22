import streamlit as st

from personal_cv.config import DESCRIPTION, NAME, PROFILE_PIC
from personal_cv.utils import display_ed, get_hard_skills

col1, col2 = st.columns(2, gap='small', vertical_alignment='center')
with col1:
    st.image(PROFILE_PIC, use_container_width=True, width=300)

with col2:
    st.title(NAME, anchor=False)
    st.write(DESCRIPTION)
    st.write('Full time work, 100% remote')

get_hard_skills()
display_ed()
