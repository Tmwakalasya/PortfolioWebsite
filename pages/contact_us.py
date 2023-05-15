import streamlit as st
from send_email import send_email
import pandas as pd
options = pd.read_csv("Pages/topics.csv")
st.title("Contact me")
with st.form("Contact me",clear_on_submit=True):
    user_email = st.text_input("Please insert your email below")
    topic = st.selectbox('What topic would you like to discuss?',(options))
    message = st.text_area("Please leave me a message")
    message = f"""\
Subject: New email from {user_email}

From:{user_email}
Topic:{topic}
{message}
"""
    send_button = st.form_submit_button(label='send message',help='send note')
    if send_button:
        send_email(message)
        st.info("Your email was sent successfully:")

