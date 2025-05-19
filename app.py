import streamlit as st
import sys

from src.config import CSS_DIR, load_css, init_locale, load_translations
from src.navigation import Page, Navigation
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.types import _


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
    projects_page = Page(
        path="src/pages/projects.py", title=_("My projects"), icon="🔨"
    )

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
