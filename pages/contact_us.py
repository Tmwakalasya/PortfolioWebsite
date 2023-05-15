import streamlit as st
from send_email import send_email
st.title("Contact me")
with st.form("Contact me",clear_on_submit=True):
    user_email = st.text_input("Please insert your email below")
    message = st.text_area("Please leave me a message")
    message = f"""\
Subject: New email from {user_email}

From:{user_email}
{message}
"""
    send_button = st.form_submit_button(label='send message',help='send note')
    if send_button:
        send_email(message)
        st.info("Your email was sent successfully:")

