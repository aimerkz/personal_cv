import gettext
from typing import Callable

translate: Callable[[str], str] = gettext.gettext
