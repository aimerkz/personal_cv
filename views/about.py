import streamlit as st

from config import AGE, DESCRIPTION, NAME, profile_pic, resume, resume_file
from utils import get_cv_info, get_hard_skills


col1, col2 = st.columns(2, gap='small', vertical_alignment='center')
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.title(NAME, anchor=False)
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
