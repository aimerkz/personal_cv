import streamlit as st

from src.utils import display_work_history

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.types import _


def work_history_page() -> None:
    st.title(_("Work History"))
    display_work_history()


work_history_page()
