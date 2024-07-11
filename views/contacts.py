import asyncio
import streamlit as st

from bot import send_message
from forms.contact_form import contact_form
from utils import get_contacts_info


@st.experimental_dialog('Contact Me')
def show_contact_form():
    contact_form()


st.title('Contacts')
get_contacts_info()
st.write('\n')
st.subheader('You can write to my bot in telegram:')

if st.button('Send'):
    show_contact_form()
