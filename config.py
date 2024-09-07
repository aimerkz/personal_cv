import streamlit as st

from pathlib import Path
from PIL import Image

# Dirs
current_dir = Path(__file__).parent
css_dir = current_dir / 'styles' / 'main.css'
profile_image = current_dir / 'static' / 'profile.png'


# General info
PAGE_TITLE = 'CV Artem Merkulov'
PAGE_ICON = ':coffee:'
NAME = 'Artem Merkulov'
DESCRIPTION = 'Python Backend Developer'
EMAIL = 'artem-merk96@yandex.ru'

SOCIAL_MEDIA = {
    'GitHub': 'https://github.com/aimerkz',
    'LinkedIn': 'https://www.linkedin.com/in/artem-merkulov-0133b328b/',
    'HabrCareer': 'https://career.habr.com/artyommerkulov',
}

SOCIAL_MEDIA_ICONS = {
    'LinkedIn': '💼',
    'GitHub': '💻',
    'HabrCareer': '💺',
}

TELEGRAM_LINK = 'https://t.me/aimerkulov96'

profile_pic = Image.open(profile_image)
