import pandas
import streamlit as st
from send_email import send_email

st.header("Contact Us!")

topic_options = pandas.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Your e-mail address")
    user_topic = st.selectbox("What topic do you want to discuss?", options=topic_options)
    raw_message = st.text_area("Your message")
    message = f"""Subject: New email from {user_email}

From: {user_email}
Topic: {user_topic}
{raw_message}
"""
    message = message.encode("utf-8")
    email_button = st.form_submit_button("Submit")
    if email_button:
        send_email(message)
        st.info("Your e-mail was sent successfully!")
