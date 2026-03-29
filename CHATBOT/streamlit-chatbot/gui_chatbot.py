import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)
messages=[]
st.title("an amazing chatbot")
if "messages" not in st.session_state:
    st.session_state.messages = []
user_input=st.chat_input("you:")

if user_input:
    st.session_state.messages.append({"role":"user","content":user_input})
    response =client.chat.completions.create(
    model= "google/gemma-3-4b-it:free",
    messages=st.session_state.messages
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    st.write(f"Bot: {reply}\n")