import json
from io import BytesIO
from typing import TYPE_CHECKING, Any

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

if TYPE_CHECKING:
    from src.types import translate as _


def get_hard_skills() -> None:
    st.subheader(_("Hard Skills"))

    skills_data = [
        {
            "icon": "👩‍💻",
            "category": _("Programming"),
            "items": ["Python", "Go ({})".format(_("minimal base")), "SQL"],
        },
        {
            "icon": "💻",
            "category": _("Frameworks and ORMs"),
            "items": [
                "Django + Django ORM",
                "DRF",
                "FastAPI",
                "Flask",
                "Litestar",
                "aiogram",
                "Piccolo ORM",
            ],
        },
        {
            "icon": "🗄️",
            "category": _("Databases"),
            "items": ["Postgres", "MySQL", "Redis"],
        },
        {
            "icon": "🎲",
            "category": _("Tests"),
            "items": ["unittest", "pytest", "pytest_mock", "factory_boy"],
        },
        {
            "icon": "⌨️",
            "category": _("OS and instruments"),
            "items": ["Ubuntu", "Pycharm", "Jira", "Confluence", "GitHub", "Gitlab"],
        },
        {
            "icon": "💾",
            "category": _("Infrastructure"),
            "items": ["Docker", "docker-compose", "nginx"],
        },
        {
            "icon": "🔎",
            "category": _("Others"),
            "items": [
                "Celery",
                "Flower",
                "Sphinx",
                "GraphQL",
                "asyncio",
                "re",
                "argparse",
                "BeautifulSoup4",
                "openpyxl",
                "poetry",
                "uv",
                "pandas",
                "numpy",
                "setuptools",
                "streamlit",
                "pydantic",
                "marshmallow",
            ],
        },
    ]

    result = "\n".join(
        f"- {item['icon']} {item['category']}: {', '.join(item['items'])}"
        for item in skills_data
    )

    st.write(result)


@st.cache_data(show_spinner=False)
def load_data(file_dir: str) -> Any:
    with open(file_dir, "r", encoding="utf-8") as file:
        return json.load(file)


def display_ed() -> None:
    data = load_data(ED_DIR)
    st.header(_("Education"))
    current_lang = st.session_state.get("lang_code", "en")

    for item in data["education"]:
        st.write(
            f"**{item['degree'][current_lang]} ({item['year']}):** "
            f"{item['university'][current_lang]}, {item['field'][current_lang]}"
        )

    st.header(_("Courses and Certifications"))
    for item in data["courses"]:
        st.write(
            f"**{item['course']} ({item['year']}):** [{item['field'][current_lang]}]({item['link']})"
        )


def display_work_history() -> None:
    data = load_data(WORK_DIR)
    current_lang = st.session_state.get("lang_code", "en")

    for job in data["work_history"]:
        st.subheader(f":briefcase: [{job['company'][current_lang]}]({job['link']})")
        st.write(f"{job['period'][current_lang]}")

        st.write("{} {}".format(_("**Role:**"), job["role"][current_lang]))

        st.write(_("**Responsibilities:**"))
        for responsibility in job["responsibilities"][current_lang]:
            st.write(f" - ► {responsibility}")


def display_projects() -> None:
    data = load_data(PROJECTS_DIR)
    current_lang = st.session_state.get("lang_code", "en")

    for project in data["projects"]:
        st.subheader(f":package: [{project['name'][current_lang]}]({project['link']})")
        st.write(f"{project['description'][current_lang]}")
        st.write(_("**Technologies:**"))
        for technology in project["technologies"]:
            st.write(f" - ► {technology}")


def get_qr_code() -> None:
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

    st.image(img, width=300, caption=_("Scan the code"))


def _get_social_media_links() -> None:
    cols = st.columns(len(SOCIAL_MEDIA))

    for col, (platform, link) in zip(cols, SOCIAL_MEDIA.items(), strict=False):
        with col:
            st.link_button(
                label=f"{SOCIAL_MEDIA_ICONS[platform]} {platform}",
                url=link,
                use_container_width=True,
                help=_("My {platform} profile").format(platform=platform),
            )


def get_contacts_info() -> None:
    _get_social_media_links()

    if st.toggle(
        label=_("Telegram QR code"),
        key="show_qr_code",
        help=_("Click to get a QR code"),
    ):
        get_qr_code()
