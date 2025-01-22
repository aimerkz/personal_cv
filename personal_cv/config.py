from pathlib import Path
from PIL import Image

# Dirs
CURRENT_DIR = Path(__file__).parent
CSS_DIR = CURRENT_DIR / 'styles' / 'main.css'
PROFILE_IMAGE = CURRENT_DIR / 'static' / 'profile.png'
ED_DIR = CURRENT_DIR / 'static' / 'education.json'
WORK_DIR = CURRENT_DIR / 'static' / 'work_history.json'


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
PROFILE_PIC = Image.open(PROFILE_IMAGE)
