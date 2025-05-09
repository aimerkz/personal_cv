from pathlib import Path

import streamlit as st
from PIL import Image

# Dirs
CURRENT_DIR = Path(__file__).parent
CSS_DIR = CURRENT_DIR / "styles" / "main.css"
PROFILE_IMAGE = CURRENT_DIR / "static" / "profile.png"
ED_DIR = CURRENT_DIR / "static" / "education.json"
WORK_DIR = CURRENT_DIR / "static" / "work_history.json"
PROJECTS_DIR = CURRENT_DIR / "static" / "projects.json"


# General info
PAGE_TITLE = "CV Artem Merkulov"
PAGE_ICON = ":coffee:"
NAME = "Artem Merkulov"
DESCRIPTION = "Python Backend Developer"
EMAIL = "artem-merk96@yandex.ru"

SOCIAL_MEDIA = {
    "GitHub": "https://github.com/aimerkz",
    "LinkedIn": "https://www.linkedin.com/in/artem-merkulov-0133b328b/",
    "HabrCareer": "https://career.habr.com/artyommerkulov",
}

SOCIAL_MEDIA_ICONS = {
    "LinkedIn": "💼",
    "GitHub": "💻",
    "HabrCareer": "💺",
}

TELEGRAM_LINK = "https://t.me/aimerkulov96"


def load_profile_image():
    try:
        with Image.open(PROFILE_IMAGE) as img:
            img.verify()
    except FileNotFoundError:
        st.error("Image not found")
        raise
    except OSError:
        st.error("Some problem with image")
        raise
    return Image.open(PROFILE_IMAGE)


@st.cache_data(max_entries=1, show_spinner=False)
def load_css(css_path):
    try:
        with open(css_path, mode="r") as css_file:
            css_text = css_file.read()
        st.markdown(f"<style>{css_text}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("CSS file not found")
        raise
    except OSError as e:
        st.error(f"An error occurred while loading CSS: {e}")
        raise
