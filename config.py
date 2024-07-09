from pathlib import Path
from PIL import Image

# Dirs
current_dir = Path(__file__).parent
css_dir = current_dir / 'styles' / 'main.css'
profile_image = current_dir / 'static' / 'profile.jpg'
resume_file = current_dir / 'static' / 'Artem Merkulov CV.pdf'


# General
PAGE_TITLE = 'CV Artem Merkulov'
PAGE_ICON = ':coffee:'
NAME = 'Artem Merkulov'
DESCRIPTION = 'Python Backend Developer'
AGE = 28
EMAIL = 'artem-merk96@yandex.ru'
SOCIAL_MEDIA = {
    'Telegram': 'https://t.me/aimerkulov96',
    'GitHub': 'https://github.com/aimerkz',
    'LinkedIn': 'https://www.linkedin.com/in/artem-merkulov-0133b328b/',
    'HabrCareer': 'https://career.habr.com/artyommerkulov',
}

# Load resume
with open(resume_file, 'rb') as resume:
    resume = resume.read()

profile_pic = Image.open(profile_image)
