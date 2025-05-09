import telebot
import pytest

from src.config import NAME, DESCRIPTION, load_profile_image
from src.pages.about import about_page
from src.pages.projects import project_page
from src.pages.work_history import work_history_page
from src.pages.contacts import contacts_page

from logic import assert_contacts_page


def test_pages_exist(app):
    pages = [
        "src/pages/about.py",
        "src/pages/work_history.py",
        "src/pages/contacts.py",
        "src/pages/projects.py",
    ]

    navigation = app.session_state.filtered_state.get("navigation")
    assert navigation, "Navigation object not found in session_state"

    for page in pages:
        sidebar_text = " ".join(app.sidebar.text.values)
        assert "🍀 by Artem Merkulov" in sidebar_text, (
            f"Page {page} did not load correctly"
        )

        nav_titles = [p.title for section in navigation.pages for p in section[1]]

        assert any(
            title in nav_titles
            for title in ["About Me", "Work history", "Contacts", "My projects"]
        ), f"Title not found for {page}"


def test_about_page(
    mock_about_st, mock_about_page_attrs, mock_get_hard_skills, mock_display_ed
):
    about_page()
    mock_about_st.columns.assert_called_once_with(
        2, gap="small", vertical_alignment="center"
    )

    with mock_about_st.columns[0]:
        mock_about_st.image.assert_called_once_with(
            load_profile_image(), use_container_width=True, width=300
        )

        mock_about_st.title.assert_called_once_with(NAME, anchor=False)
        assert mock_about_st.write.call_count == 2
        calls = [args[0] for args, _ in mock_about_st.write.call_args_list]
        assert DESCRIPTION in calls
        assert "Full time work, 100% remotely" in calls

    mock_get_hard_skills.assert_called_once()
    mock_display_ed.assert_called_once()


def test_projects_page(
    mock_projects_st, mock_projects_page_attrs, mock_display_projects
):
    project_page()
    assert (
        mock_projects_st.title.return_value
        == mock_projects_page_attrs.title.return_value
    )
    mock_display_projects.assert_called_once()


def test_work_history_page(
    mock_work_history_st, mock_work_history_page_attrs, mock_display_work_history
):
    work_history_page()
    assert (
        mock_work_history_st.title.return_value
        == mock_work_history_page_attrs.title.return_value
    )
    mock_display_work_history.assert_called_once()


def test_contacts_page_without_send_message(
    mock_contacts_st,
    mock_contacts_page_attrs,
    mock_display_contacts_info,
    mock_show_contact_form,
    mock_not_send_bot_message,
):
    contacts_page()

    assert_contacts_page(mock_contacts_st, mock_contacts_page_attrs)

    mock_display_contacts_info.assert_called_once()
    mock_show_contact_form.assert_called_once()
    mock_not_send_bot_message.assert_not_called()


def test_contacts_page_with_send_message(
    mock_contacts_st,
    mock_contacts_page_attrs,
    mock_display_contacts_info,
    mock_show_contact_form,
    mock_send_bot_message,
):
    message = mock_contacts_st.session_state["message_data"]
    success_flag = mock_contacts_st.success
    contacts_page()

    assert_contacts_page(mock_contacts_st, mock_contacts_page_attrs)

    mock_display_contacts_info.assert_called_once()
    mock_show_contact_form.assert_called_once()
    mock_send_bot_message.assert_called_once_with(message)
    assert success_flag is not None


def test_contacts_page_with_error_send_message(
    mock_contacts_st,
    mock_contacts_page_attrs,
    mock_display_contacts_info,
    mock_show_contact_form,
    mock_send_bot_message_with_error,
):
    message = mock_contacts_st.session_state["message_data"]

    with pytest.raises(telebot.apihelper.ApiException):
        contacts_page()

    assert_contacts_page(mock_contacts_st, mock_contacts_page_attrs)

    mock_display_contacts_info.assert_called_once()
    mock_show_contact_form.assert_called_once()
    mock_send_bot_message_with_error.assert_called_once_with(message)
