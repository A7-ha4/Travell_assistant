from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
import os

model = OllamaEmbeddings(model="mxbai-embed-large")

persist_directory = os.path.join("Chroma_db","Data")

vector_store = Chroma(
    embedding_function=model,
    persist_directory=persist_directory,
    collection_name="Traveller_ai"
)

def store(result, ques) :
    doc = Document(page_content=result, metadata={"ques" : ques})

    vector_store.add_documents([doc])

retriever = vector_store.as_retriever(
    search_kwargs={"k":1}
)
