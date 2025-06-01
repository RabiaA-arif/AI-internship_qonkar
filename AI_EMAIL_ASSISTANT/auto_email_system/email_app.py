import streamlit as st
import imaplib
import email
from email.header import decode_header
from email.utils import parseaddr
import smtplib
from email.mime.text import MIMEText
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
username = st.secrets("EMAIL_ID")
password = st.secrets("EMAIL_PASSWORD")
api_gemini_key = st.secrets("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_gemini_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def fetch_latest_unread_email():
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(username, password)
    imap.select("INBOX")
    status, messages = imap.search(None, "UNSEEN")
    email_ids = messages[0].split()
    if email_ids:
        latest_id = email_ids[-1]
        status, msg_data = imap.fetch(latest_id, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else "utf-8")
        from_ = parseaddr(msg["From"])[1]

        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode(errors="ignore")
                    break
        else:
            body = msg.get_payload(decode=True).decode(errors="ignore")

        imap.logout()
        return from_, subject, body
    imap.logout()
    return None, None, "No unread emails found."

def generate_reply(email_text):
    prompt = f"You are an AI assistant. Read this email and write a polite, professional reply.\n\nEmail:\n{email_text}\n\nReply:"
    response = model.generate_content(prompt)
    return response.text.strip()

def send_reply(to_address, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = "RE: " + subject
    msg["From"] = username
    msg["To"] = to_address

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(username, password)
        server.send_message(msg)

# Streamlit UI
st.title("📧 AI Email Auto-Responder")

if st.button("📥 Fetch Latest Unread Email"):
    from_, subject, body = fetch_latest_unread_email()
    if from_:
        st.session_state.from_ = from_
        st.session_state.subject = subject
        st.session_state.body = body
        st.success("Email fetched successfully!")
    else:
        st.warning(body)

if "body" in st.session_state:
    st.subheader("Email Content")
    st.write(st.session_state.body)

    if st.button("⚡ Generate AI Reply"):
        reply = generate_reply(st.session_state.body)
        st.session_state.reply = reply
        st.success("Reply generated!")

if "reply" in st.session_state:
    st.subheader("AI-Generated Reply")
    st.text_area("Reply", value=st.session_state.reply, height=200)

    if st.button("📤 Send Reply"):
        send_reply(
            to_address=st.session_state.from_,
            subject=st.session_state.subject,
            body=st.session_state.reply,
        )
        st.success("Reply sent successfully!")
