from unittest.mock import MagicMock


def assert_contacts_page(
    mock_contacts_st: MagicMock, mock_contacts_page_attrs: MagicMock
) -> None:
    assert (
        mock_contacts_st.title.return_value == mock_contacts_page_attrs.title.return_value
    )
    assert (
        mock_contacts_st.write.return_value == mock_contacts_page_attrs.write.return_value
    )
    assert (
        mock_contacts_st.subheader.return_value
        == mock_contacts_page_attrs.subheader.return_value
    )
