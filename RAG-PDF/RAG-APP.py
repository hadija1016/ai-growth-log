from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader("example.pdf")
docs=loader.load()
print(f"total pages:{len(docs)}")
print(f"page 1 content:{docs[0].page_content[:100]}")
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50,length_function=len,separators=["\n\n","\n"," ",""])
text=text_splitter.create_documents([doc.page_content for doc in docs])
print(f"total chunks:{len(text)}")
print(f"chunk 1 content:{text[0].page_content[100:150]}")

from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
from langchain_community.vectorstores import Chroma
vectorstore=Chroma.from_documents(
    documents=text,
    embedding=embeddings
)
results=vectorstore.similarity_search("What is an activation function?")
print(results[0].page_content)
#from langchain.chains import RetrievalQA
#from langchain_openai import ChatOpenAI
context="\n\n".join([result.page_content for result in results])
print(context)  
prompt = f"""
You are a helpful AI assistant.

Use ONLY the information from the context below to answer the question.
Do not use prior knowledge.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
What is an activation function?

Answer:
"""
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)
response = client.chat.completions.create(
    model="google/gemma-3-4b-it:free",
    messages=[{"role": "user", "content": prompt}]
)
print(response.choices[0].message.content)