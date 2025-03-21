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
