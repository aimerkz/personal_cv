import streamlit as st
import sys

from src.config import CSS_DIR, load_css
from src.navigation import Page, Navigation


def main() -> None:
    about_page = Page(
        path="src/pages/about.py", title="About Me", icon="☕", default=True
    )
    work_history_page = Page(
        path="src/pages/work_history.py", title="Work history", icon="🧑‍💼"
    )
    contacts_page = Page(path="src/pages/contacts.py", title="Contacts", icon="📒")
    projects_page = Page(path="src/pages/projects.py", title="My projects", icon="🔨")

    navigation = Navigation()
    navigation.add_section("Home", [about_page])
    navigation.add_section("Info", [work_history_page, contacts_page])
    navigation.add_section("Projects", [projects_page])

    if "pytest" in sys.modules or any("pytest" in arg for arg in sys.argv):
        st.session_state["navigation"] = navigation

    load_css(CSS_DIR)
    st.sidebar.text("🍀 by Artem Merkulov")
    navigation.run()


if __name__ == "__main__":
    main()
