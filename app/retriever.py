from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from app.config import OPENAI_API_KEY

def get_retriever(splits):
    """
    Create a retriever using the provided document splits.
    
    Args:
        splits (list): List of document splits.
    
    Returns:
        Retriever: A retriever object configured for similarity search.
    """
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large", api_key=OPENAI_API_KEY)
    vectorstore = Chroma.from_documents(splits, embeddings)
    return vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})