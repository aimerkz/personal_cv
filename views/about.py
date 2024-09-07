import streamlit as st

from config import DESCRIPTION, NAME, profile_pic
from utils import get_cv_info, get_hard_skills

col1, col2 = st.columns(2, gap='small', vertical_alignment='center')
with col1:
    st.image(profile_pic, use_column_width=True, width=300)

with col2:
    st.title(NAME, anchor=False)
    st.write(DESCRIPTION)
    st.write('Full time work, 100% remote')

get_hard_skills()
get_cv_info()
