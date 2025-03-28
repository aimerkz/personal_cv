from unittest.mock import MagicMock

from streamlit.testing.v1 import AppTest
import pytest


@pytest.fixture(scope="session")
def app() -> AppTest:
    app = AppTest.from_file("../app.py")
    app.run()
    return app


@pytest.fixture
def mock_st_about(mocker):
    mock_st = mocker.patch("src.pages.about.st")
    return mock_st


@pytest.fixture
def mock_columns_about(mock_st_about):
    mock_columns = [MagicMock(), MagicMock()]
    mock_st_about.columns.return_value = mock_columns
    return mock_columns


@pytest.fixture
def mock_get_hard_skills(mocker):
    return mocker.patch("src.pages.about.get_hard_skills")


@pytest.fixture
def mock_display_ed(mocker):
    return mocker.patch("src.pages.about.display_ed")
