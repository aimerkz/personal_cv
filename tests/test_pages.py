from src.config import PROFILE_PIC, NAME, DESCRIPTION
from src.pages.about import about_page


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
    mock_st_about, mock_columns_about, mock_get_hard_skills, mock_display_ed
):
    about_page()
    mock_st_about.columns.assert_called_once_with(
        2, gap="small", vertical_alignment="center"
    )

    with mock_columns_about[0]:
        mock_st_about.image.assert_called_once_with(
            PROFILE_PIC, use_container_width=True, width=300
        )

        mock_st_about.title.assert_called_once_with(NAME, anchor=False)
        assert mock_st_about.write.call_count == 2
        calls = [args[0] for args, _ in mock_st_about.write.call_args_list]
        assert DESCRIPTION in calls
        assert "Full time work, 100% remote" in calls

    mock_get_hard_skills.assert_called_once()
    mock_display_ed.assert_called_once()
