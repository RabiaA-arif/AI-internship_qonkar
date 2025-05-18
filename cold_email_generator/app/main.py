import streamlit as st
import trafilatura
from langchain.text_splitter import RecursiveCharacterTextSplitter
from chains import Chain
from portfolio import Portfolio
from util import clean_text


def fetch_text_from_url(url):
    """Use trafilatura to fetch and clean webpage text."""
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        return None
    return trafilatura.extract(downloaded)


def split_text(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", " "]
    )
    return text_splitter.split_text(text)

import streamlit as st
import base64

def create_streamlit_app(llm, portfolio):
    # Set page config
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")

    # Custom CSS for background + styling
    

    st.title("📧 Cold Email Generator")

    url_input = st.text_input("Enter job listing URL:", value="https://www.guru.com/m/find/freelance-jobs/web-data-scraping/")
    job_role = st.text_input("What job role are you targeting?", placeholder="e.g. Frontend Developer")

    submit_button = st.button("Generate Cold Email")

    if submit_button:
        if not job_role.strip():
            st.warning("⚠️ Please enter a job role.")
            return

        try:
            st.info("🔍 Fetching content from the URL...")
            raw_text = fetch_text_from_url(url_input)
            if not raw_text:
                st.error("⚠️ Failed to extract content from the URL.")
                return

            st.info("🧠 Preparing cold email based on your role...")
            cleaned = clean_text(raw_text)
            chunks = split_text(cleaned)

            portfolio.load_portfolio()
            links = portfolio.query_links([job_role])

            job_description = chunks[0]
            email = llm.write_mail(job_description, links, job_role)

            if email:
                st.success("✅ Cold email generated:")
                # Format email markdown
                formatted_email = f"""\
                <pre style="background-color: white; padding: 1.5rem; border-radius: 1rem; font-size: 16px; line-height: 1.5;">
                {email}
                </pre>"""
                st.markdown(formatted_email, unsafe_allow_html=True)
            else:
                st.warning("⚠️ No email content generated. Please check your LLM response.")

        except Exception as e:
            st.error(f"❌ An error occurred: {e}")



if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio)
    
    
