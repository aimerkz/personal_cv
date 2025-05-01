from src.config import PROFILE_PIC, NAME, DESCRIPTION
from src.pages.about import about_page
from src.pages.projects import project_page
from src.pages.work_history import work_history_page
from src.pages.contacts import contacts_page


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
    mock_about_st, mock_columns_about, mock_get_hard_skills, mock_display_ed
):
    about_page()
    mock_about_st.columns.assert_called_once_with(
        2, gap="small", vertical_alignment="center"
    )

    with mock_columns_about[0]:
        mock_about_st.image.assert_called_once_with(
            PROFILE_PIC, use_container_width=True, width=300
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


def test_contacts_page(
    mock_contacts_st,
    mock_contacts_page_attrs,
    mock_display_contacts_info,
    mock_tg_bot,
    mock_show_contact_form,
):
    contacts_page()
    assert (
        mock_contacts_st.title.return_value
        == mock_contacts_page_attrs.title.return_value
    )
    assert (
        mock_contacts_st.write.return_value
        == mock_contacts_page_attrs.write.return_value
    )
    assert (
        mock_contacts_st.subheader.return_value
        == mock_contacts_page_attrs.subheader.return_value
    )
