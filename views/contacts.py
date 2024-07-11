import streamlit as st

from utils import get_contacts_info


st.title('Contacts')
get_contacts_info()
st.write('\n')
st.subheader('You can write to me in telegram:')

if 'text_input' not in st.session_state:
    st.session_state['my_input'] = ''

text = st.text_input(
    label='Type your message and click Send',
    placeholder='Hi',
)
submit = st.button('Send')
if submit:
    st.session_state['text_input'] = text
    st.write('You have entered: ', text)
