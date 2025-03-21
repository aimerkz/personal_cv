import json
from io import BytesIO

import qrcode
import streamlit as st
from PIL import Image

from src.config import (
    ED_DIR,
    PROJECTS_DIR,
    SOCIAL_MEDIA,
    SOCIAL_MEDIA_ICONS,
    TELEGRAM_LINK,
    WORK_DIR,
)


@st.cache_data(max_entries=1, show_spinner=False)
def get_hard_skills():
    st.subheader("Hard Skills")
    st.write(
        """
    - 👩‍💻 Programming: Python, Go (minimal base), SQL
    - 💻 Frameworks and ORMs: Django + Django ORM, DRF, FastAPI, Flask, aiogram
    - 🗄️ Databases: Postgres, MySQL, Redis
    - 🎲 Tests: unittest, pytest, pytest_mock, factory_boy
    - ⌨️ OS and instruments: Ubuntu, Pycharm, Jira, Confluence, GitHub, Gitlab
    - 💾 Infrastructure: Docker, docker-compose, nginx
    - 🔎 Others: Celery, Flower, Sphinx, GraphQL, re, argparse, BeautifulSoup4, openpyxl, poetry, 
                 pandas, numpy, setuptools, streamlit, pydantic, marshmallow
    """
    )


@st.cache_data(max_entries=1, show_spinner=False)
def load_data(file_dir: str):
    with open(file_dir, "r", encoding="utf-8") as file:
        return json.load(file)


def display_ed():
    data = load_data(ED_DIR)
    st.header("Education")

    for item in data["education"]:
        st.write(
            f"**{item['degree']} ({item['year']}):** {item['university']}, {item['field']}"
        )

    st.header("Courses and Certifications")
    for item in data["courses"]:
        st.write(
            f"**{item['course']} ({item['year']}):** [{item['field']}]({item['link']})"
        )


def display_work_history():
    data = load_data(WORK_DIR)

    for job in data["work_history"]:
        st.subheader(f":briefcase: [{job['company']}]({job['link']})")
        st.write(f"{job['period']}")
        st.write(f"**Role:** {job['role']}")
        st.write("**Responsibilities:**")
        for responsibility in job["responsibilities"]:
            st.write(f" - ► {responsibility}")


def display_projects():
    data = load_data(PROJECTS_DIR)

    for project in data["projects"]:
        st.subheader(f":package: [{project['name']}]({project['link']})")
        st.write(f"{project['description']}")
        st.write("**Technologies:**")
        for technology in project["technologies"]:
            st.write(f" - ► {technology}")


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

    img = qr.make_image(fill_color="black", back_color="white")

    buf = BytesIO()
    img.save(buf)
    buf.seek(0)
    img = Image.open(buf)

    st.image(img, width=300, caption="Scan the code")


def get_contacts_info():
    col = st.columns(1)[0]
    links = " | ".join(
        f"[{platform} {SOCIAL_MEDIA_ICONS[platform]}]({link})"
        for platform, link in SOCIAL_MEDIA.items()
    )
    col.markdown(links, unsafe_allow_html=True)

    if "show_content" not in st.session_state:
        st.session_state.show_content = False

    if st.button("Get Telegram QR Code"):
        st.session_state.show_content = not st.session_state.show_content

    if st.session_state.show_content:
        get_qr_code()
