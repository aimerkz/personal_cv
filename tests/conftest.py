from unittest.mock import MagicMock
from typing import Any

from streamlit.testing.v1 import AppTest
import pytest
import telebot
import gettext

from src.bot import TelegramBot


@pytest.fixture(scope="session", autouse=True)
def mock_localizer():
    translation = gettext.translation(
        domain="messages", localedir="src/locale", languages=["en"], fallback=True
    )
    translation.install("gettext")


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
def mock_send_bot_message_factory(mock_tg_bot: TelegramBot, mocker, mock_contacts_st):
    def _mock_send_message(message: str, is_send: bool = False) -> MagicMock:
        if is_send:
            mock_contacts_st.session_state = {"message_data": message}
            mock_contacts_st.success = "Message sent"
        mock_send = mocker.patch("src.bot.tg_bot.send_message")
        return mock_send

    return _mock_send_message


@pytest.fixture
def mock_send_bot_message(mock_send_bot_message_factory) -> MagicMock:
    return mock_send_bot_message_factory("message", True)


@pytest.fixture
def mock_not_send_bot_message(mock_send_bot_message_factory) -> MagicMock:
    return mock_send_bot_message_factory("message")


@pytest.fixture
def mock_send_bot_message_with_error(mock_send_bot_message_factory) -> MagicMock:
    mock_send = mock_send_bot_message_factory("message", True)
    mock_send.side_effect = telebot.apihelper.ApiException("error", "send_message", {})
    return mock_send


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
def mock_show_contact_form(mock_display_func_factory) -> MagicMock:
    return mock_display_func_factory("src.pages.contacts.show_contact_form")


@pytest.fixture
def mock_attrs_factory():
    def _mock(target_mock: MagicMock, attrs: dict[str, Any]) -> MagicMock:
        for key, value in attrs.items():
            target_mock.key.return_value = value
        return target_mock

    return _mock


@pytest.fixture
def mock_about_page_attrs(mock_attrs_factory, mock_about_st) -> MagicMock:
    mock = mock_attrs_factory(mock_about_st, {})
    mock.columns.return_value = [MagicMock(), MagicMock()]
    return mock


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
