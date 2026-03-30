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