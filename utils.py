from io import BytesIO

import qrcode
import streamlit as st
from PIL import Image

from config import SOCIAL_MEDIA, SOCIAL_MEDIA_ICONS, TELEGRAM_LINK


@st.cache_data(max_entries=1, show_spinner=False)
def get_hard_skills():
    st.subheader("Hard Skills")
    st.write(
        """
    - 👩‍💻 Programming: Python, SQL, pytest, unittest, pytest_mock, factory_boy, pandas, numpy
    - 💻 Frameworks and ORMs: Django + Django ORM, DRF, FastAPI, Flask, Celery, Flower
    - 🗄️ Databases: Postgres, MySQL, Redis
    - ⌨️ OS and instruments: Ubuntu, Pycharm, Jira, Confluence, GitHub, Gitlab
    - 💾 Infrastructure: Docker, docker-compose, nginx
    - 🔎 Others: Sphinx, GraphQL, re, argparse, BeautifulSoup4, openpyxl, poetry, setuptools
    """
    )


@st.cache_data(max_entries=1, show_spinner=False)
def get_cv_info():
    st.header("Education")
    st.write(
        """
        **Master's Degree (2021):** Kaluga State University named after K. E. Tsiolkovsky, Kaluga  
        **Field:** Russian as a Foreign Language \n
        **Bachelor's Degree (2018):** Kaluga State University named after K. E. Tsiolkovsky, Kaluga  
        **Field:** Russian Language and Literature  
    """
    )

    st.header("Courses and Certifications")
    st.write(
        """
        **Yandex Practicum (2022):** Python Backend Developer \n
        **Stepik (2022):** Basics of Python / Basics of SQL / Introduction to Databases \n
        **GeekBrains (2022):** Basic Git Course  
    """
    )


@st.cache_data(max_entries=1, show_spinner=False)
def get_work_history():
    st.subheader(':briefcase: Spider Group')
    st.write('05/2024 - Present')
    st.write(
        """
        **Role:** Python Backend Developer  
        **Responsibilities:**
        - ► Improved backend of an online store using FastApi and DRF + Redis;
        - ► Implemented SMS and PyJWT-based authorization and authentication;
        - ► Configured full-text search using Sphinx;
        - ► Developed APIs for routine tasks;
        - ► Wrote raw SQL queries and worked with Django ORM;
        - ► Supported and optimized local development;
        - ► Conducted code reviews and refactoring.
    """
    )
    st.write('\n')
    st.subheader(":briefcase: Napoleon IT")
    st.write('06/2023 - 07/2024')
    st.write(
        """
        **Role:** Backend Python Developer  
        **Responsibilities:**
        - ► Developed backend platform on FastApi for business process automation at Gloria Jeans;
        - ► Implemented and supported sections for store planning;
        - ► Developed APIs for routine tasks;
        - ► Developed calculation methods using Pandas and Numpy;
        - ► Wrote GraphQL queries;
        - ► Wrote tests using pytest and pytest_mock;
        - ► Supported and optimized local development;
        - ► Developed backend platform on DRF + Celery + Redis for Lenta;
        - ► Handled data import and export using openpyxl;
        - ► Covered code with tests using pytest and factory_boy;
        - ► Conducted code reviews and refactoring;
        - ► Developed a parser for md and yml templates using re, argparse, yaml, BeautifulSoup4.
    """
    )

    st.write('\n')
    st.subheader(':briefcase: High Technologies and Strategic Systems')
    st.write('04/2022 - 06/2023')
    st.write(
        """
        **Role:** Programmer  
        **Responsibilities:**
        - ► Developed REST API using Django and DRF;
        - ► Covered code with tests using python unittest;
        - ► Created packages using setuptools;
        - ► Conducted code reviews and refactoring.
    """
    )


@st.cache_data(persist=True, max_entries=1, show_spinner=False)
def get_qr_code():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=6,
        border=4,
    )

    qr.add_data(TELEGRAM_LINK)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')

    buf = BytesIO()
    img.save(buf)
    buf.seek(0)
    img = Image.open(buf)

    st.image(img, width=300, caption='Scan the code')


def get_contacts_info():
    col = st.columns(1)[0]
    links = " | ".join(
        f"[{platform} {SOCIAL_MEDIA_ICONS[platform]}]({link})"
        for platform, link in SOCIAL_MEDIA.items()
    )
    col.markdown(links, unsafe_allow_html=True)

    if 'show_content' not in st.session_state:
        st.session_state.show_content = False

    if st.button('Get Telegram QR Code'):
        st.session_state.show_content = not st.session_state.show_content

    if st.session_state.show_content:
        get_qr_code()
