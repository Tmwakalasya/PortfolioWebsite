import streamlit as st
st.title("Contact me")
with st.form("Contact me",clear_on_submit=True):
    email = st.text_input("Please insert your email below")
    message = st.text_area("Please leave me a message")
    send_button = st.form_submit_button(label='send message',help='send note')
    # if send_button:

