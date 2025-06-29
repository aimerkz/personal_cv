import sys
from typing import TYPE_CHECKING

import streamlit as st

from src.config import CSS_DIR, init_locale, load_css, load_translations
from src.navigation import Navigation, Page

if TYPE_CHECKING:
    from src.types import translate as _


def main() -> None:
    load_translations()
    init_locale()

    about_page = Page(
        path="src/pages/about.py", title=_("About Me"), icon="☕", default=True
    )
    work_history_page = Page(
        path="src/pages/work_history.py", title=_("Work history"), icon="🧑‍💼"
    )
    contacts_page = Page(path="src/pages/contacts.py", title=_("Contacts"), icon="📒")
    projects_page = Page(path="src/pages/projects.py", title=_("My projects"), icon="🔨")

    navigation = Navigation()
    navigation.add_section(_("Home"), [about_page])
    navigation.add_section(_("Info"), [work_history_page, contacts_page])
    navigation.add_section(_("Projects"), [projects_page])

    if "pytest" in sys.modules or any("pytest" in arg for arg in sys.argv):
        st.session_state["navigation"] = navigation

    load_css(CSS_DIR)

    author = _("by Artem Merkulov")
    st.sidebar.text(f"🍀 {author}")

    navigation.run()


if __name__ == "__main__":
    main()
