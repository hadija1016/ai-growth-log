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

st.set_page_config(page_title="Lavender AI 💜", layout="centered")

import streamlit as st

st.set_page_config(page_title="Lavender AI 💜", layout="centered")

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
st.markdown('<h1 class="title">💜 LAVENDER AI 🎀</h1>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())
    loader = PyPDFLoader("temp.pdf")
    docs=loader.load()
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50,length_function=len,separators=["\n\n","\n"," ",""])
    text=text_splitter.create_documents([doc.page_content for doc in docs])
    embeddings = langchain_huggingface.HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore=Chroma.from_documents(
    documents=text,
    embedding=embeddings    
    )
    results=vectorstore.similarity_search("What is an activation function?")
    print(results[0].page_content)
    context="\n\n".join([result.page_content for result in results])
    print(context) 

    query = st.text_input("LESS GOO GURLL:")

    prompt = f"""
    You are a helpful AI assistant.

    Use ONLY the information from the context below to answer the question.
    Do not use prior knowledge.
    If the answer is not in the context, say "I don't know".
     Context:
     {context}

     Question:
    {query}
    Answer:
    """
    response = client.chat.completions.create(
     model="google/gemma-3-4b-it:free",
     messages=[{"role": "user", "content": prompt}]
)
    st.write(response.choices[0].message.content)
