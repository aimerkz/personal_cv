from typing import TYPE_CHECKING

import streamlit as st

from src.utils import display_work_history

if TYPE_CHECKING:
    from src.types import translate as _


def work_history_page() -> None:
    st.title(_("Work History"))
    display_work_history()


work_history_page()
