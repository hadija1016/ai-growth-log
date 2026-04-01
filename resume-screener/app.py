import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
import langchain_huggingface
from langchain_huggingface import HuggingFaceEmbeddings
load_dotenv()
client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

st.set_page_config(page_title="RESUME-SCREENER", layout="centered")

import streamlit as st

st.set_page_config(page_title="RESUME-SCREENER", layout="centered")

# UI Styling + Font + Title
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');

/* Background */
.stApp {
    background: linear-gradient(to right, #fbc2eb, #a18cd1);
}

/* Buttons */
.stButton>button {
    background-color: #C084FC;
    color: white;
    border-radius: 20px;
    padding: 10px 20px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #A855F7;
}

/* Title Styling */
.title {
    text-align: center;
    font-family: 'Pacifico', cursive;
    color: #9333EA;
    font-size: 48px;
}
</style>
""", unsafe_allow_html=True)

# Centered bubbly title
st.markdown('<h1 class="title"> RESUME SCREENER </h1>', unsafe_allow_html=True)
# ACTUAL CODE
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())
    loader = PyPDFLoader("temp.pdf")
    docs=loader.load()
    RESUME_TEXT="\n".join([doc.page_content for doc in docs])
    st.write(RESUME_TEXT)
    