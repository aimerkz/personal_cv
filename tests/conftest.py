from streamlit.testing.v1 import AppTest
import pytest


@pytest.fixture(scope="session")
def app() -> AppTest:
    app = AppTest.from_file("../app.py")
    app.run()
    return app


@pytest.fixture
def mock_get_hard_skills(mocker):
    return mocker.patch("src.utils.get_hard_skills")


@pytest.fixture
def mock_display_ed(mocker):
    return mocker.patch("src.utils.display_ed")


@pytest.fixture
def mock_display_work_history(mocker):
    return mocker.patch("src.utils.display_work_history")


@pytest.fixture
def mock_display_projects(mocker):
    return mocker.patch("src.utils.display_projects")
