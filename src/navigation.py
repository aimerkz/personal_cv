import streamlit as st


class Page:
    def __init__(self, path: str, title: str, icon: str, default: bool = False) -> None:
        self.path = path
        self.title = title
        self.icon = icon
        self.default = default

    def create(self) -> st.Page:
        return st.Page(self.path, title=self.title, icon=self.icon, default=self.default)


class Navigation:
    def __init__(self, pages: list[tuple[str, list[Page]]] | None = None) -> None:
        self.pages = [] if pages is None else pages.copy()

    def add_section(self, section_name: str, pages: list[Page]) -> None:
        self.pages.append((section_name, pages))

    def run(self) -> None:
        navigation_pages = {}
        for section_name, pages in self.pages:
            navigation_pages[section_name] = [page.create() for page in pages]

        pg = st.navigation(navigation_pages)
        pg.run()
