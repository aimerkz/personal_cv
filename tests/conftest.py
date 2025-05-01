from unittest.mock import MagicMock
from typing import Any

from streamlit.testing.v1 import AppTest
import pytest

from src.bot import TelegramBot


@pytest.fixture(scope="session")
def app() -> AppTest:
    app = AppTest.from_file("../app.py")
    app.run()
    return app


@pytest.fixture(scope="session")
def mock_tg_bot() -> TelegramBot:
    mock_bot = MagicMock()
    tg_bot = TelegramBot(bot=mock_bot, chat_id=123)
    return tg_bot


@pytest.fixture
def mock_st_factory(mocker):
    def _mock_st(module_path: str) -> MagicMock:
        mock_st = mocker.patch(module_path)
        return mock_st

    return _mock_st


@pytest.fixture
def mock_about_st(mock_st_factory) -> MagicMock:
    mock_st = mock_st_factory("src.pages.about.st")
    return mock_st


@pytest.fixture
def mock_projects_st(mock_st_factory) -> MagicMock:
    mock_st = mock_st_factory("src.pages.projects.st")
    return mock_st


@pytest.fixture
def mock_work_history_st(mock_st_factory) -> MagicMock:
    mock_st = mock_st_factory("src.pages.work_history.st")
    return mock_st


@pytest.fixture
def mock_contacts_st(mock_st_factory) -> MagicMock:
    mock_st = mock_st_factory("src.pages.contacts.st")
    return mock_st


@pytest.fixture
def mock_display_func_factory(mocker):
    def _mock_func(module_path: str) -> MagicMock:
        return mocker.patch(module_path)

    return _mock_func


@pytest.fixture
def mock_get_hard_skills(mock_display_func_factory) -> MagicMock:
    return mock_display_func_factory("src.pages.about.get_hard_skills")


@pytest.fixture
def mock_display_ed(mock_display_func_factory) -> MagicMock:
    return mock_display_func_factory("src.pages.about.display_ed")


@pytest.fixture
def mock_display_projects(mock_display_func_factory) -> MagicMock:
    return mock_display_func_factory("src.pages.projects.display_projects")


@pytest.fixture
def mock_display_work_history(mock_display_func_factory) -> MagicMock:
    return mock_display_func_factory("src.pages.work_history.display_work_history")


@pytest.fixture
def mock_display_contacts_info(mock_display_func_factory) -> MagicMock:
    return mock_display_func_factory("src.pages.contacts.get_contacts_info")


@pytest.fixture
def mock_columns_about(mock_about_st) -> list[MagicMock]:
    mock_columns = [MagicMock(), MagicMock()]
    mock_about_st.columns.return_value = mock_columns
    return mock_columns


@pytest.fixture
def mock_attrs_factory():
    def _mock(target_mock: MagicMock, attrs: [dict[str, Any]]) -> MagicMock:
        for key, value in attrs.items():
            target_mock.key.return_value = value
            return target_mock

    return _mock


@pytest.fixture
def mock_projects_page_attrs(mock_attrs_factory, mock_projects_st) -> MagicMock:
    return mock_attrs_factory(mock_projects_st, {"title": "Projects"})


@pytest.fixture
def mock_work_history_page_attrs(mock_attrs_factory, mock_work_history_st) -> MagicMock:
    return mock_attrs_factory(mock_work_history_st, {"title": "Work History"})


@pytest.fixture
def mock_contacts_page_attrs(mock_attrs_factory, mock_contacts_st) -> MagicMock:
    return mock_attrs_factory(
        mock_contacts_st,
        {"title": "Contacts", "write": "\n", "subheader": "Subheader"},
    )


@pytest.fixture
def mock_show_contact_form(mocker) -> MagicMock:
    return mocker.patch("src.pages.contacts.show_contact_form")
