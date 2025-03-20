import streamlit as st

from personal_cv.config import CSS_DIR, load_css


class Page:
    def __init__(self, path: str, title: str, icon: str, default: bool = False) -> None:
        self.path = path
        self.title = title
        self.icon = icon
        self.default = default

    def create(self) -> st.Page:
        return st.Page(
            self.path,
            title=self.title,
            icon=self.icon,
            default=self.default
        )


class Navigation:
    def __init__(self, pages: list[str, list[Page]] | None = None) -> None:
        self.pages = [] if pages is None else pages.copy()

    def add_section(self, section_name: str, pages: list[Page]) -> None:
        self.pages.append((section_name, pages))

    def run(self):
        navigation_pages = {}
        for section_name, pages in self.pages:
            navigation_pages[section_name] = [page.create() for page in pages]

        pg = st.navigation(navigation_pages)
        pg.run()


def main() -> None:
    about_page = Page(
        path='personal_cv/views/about.py',
        title='About Me',
        icon='☕',
        default=True
    )
    work_history_page = Page(
        path='personal_cv/views/work_history.py',
        title='Work history',
        icon='🧑‍💼'
    )
    contacts_page = Page(
        path='personal_cv/views/contacts.py',
        title='Contacts',
        icon='📒'
    )
    projects_page = Page(
        path='personal_cv/views/projects.py',
        title='My projects',
        icon='🔨'
    )

    navigation = Navigation()
    navigation.add_section('Home', [about_page])
    navigation.add_section('Info', [work_history_page, contacts_page])
    navigation.add_section('Projects', [projects_page])

    load_css(CSS_DIR)

    navigation.run()

    st.sidebar.text('🍀 by Artem Merkulov')

if __name__ == "__main__":
    main()
