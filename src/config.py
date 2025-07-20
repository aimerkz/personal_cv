import gettext
from pathlib import Path
from typing import Final

import streamlit as st

# Dirs
CURRENT_DIR = Path(__file__).parent
CSS_DIR = CURRENT_DIR / "styles" / "main.css"
PROFILE_IMAGE = CURRENT_DIR / "static" / "profile.jpg"
ED_DIR = CURRENT_DIR / "static" / "education.json"
WORK_DIR = CURRENT_DIR / "static" / "work_history.json"
PROJECTS_DIR = CURRENT_DIR / "static" / "projects.json"

PAGE_ICON: str = ":coffee:"
EMAIL: str = "artem-merk96@yandex.ru"

SOCIAL_MEDIA: Final[dict[str, str]] = {
    "GitHub": "https://github.com/aimerkz",
    "LinkedIn": "https://www.linkedin.com/in/artem-merkulov-0133b328b/",
    "HabrCareer": "https://career.habr.com/artyommerkulov",
}

SOCIAL_MEDIA_ICONS: Final[dict[str, str]] = {
    "LinkedIn": "💼",
    "GitHub": "💻",
    "HabrCareer": "💺",
}

TELEGRAM_LINK: str = "https://t.me/aimerkulov96"

LANGUAGES: Final[dict[str, str]] = {
    "English": "en",
    "Русский": "ru",
}


def init_locale() -> None:
    if "lang_code" not in st.session_state:
        st.session_state.lang_code = "en"

    prev_lang = st.session_state.lang_code

    with st.sidebar:
        selected_lang_label = st.selectbox("🌐 Select Language", list(LANGUAGES.keys()))
        selected_lang_code = LANGUAGES[selected_lang_label]
        st.session_state.lang_code = selected_lang_code

    if selected_lang_code != prev_lang:
        st.rerun()


def load_translations() -> None:
    lang_code = st.session_state.get("lang_code", "en")

    translation = gettext.translation(
        domain="messages", localedir="src/locale", languages=[lang_code], fallback=True
    )
    translation.install("gettext")


@st.cache_data(max_entries=1, show_spinner=False)
def load_css(css_path) -> None:
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
