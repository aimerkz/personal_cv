import streamlit as st

from personal_cv.bot import send_message
from personal_cv.forms.contact_form import contact_form
from personal_cv.utils import get_contacts_info


@st.dialog('Contact Me')
def show_contact_form():
    contact_form()


st.title('Contacts')
get_contacts_info()
st.write('\n')

st.subheader('Also you can write to my bot in Telegram:')

if st.button('Send'):
    show_contact_form()

if 'message_data' in st.session_state:
    message = st.session_state.pop('message_data')
    send_message(message)
