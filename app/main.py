from app.rag_chain import create_rag_chain
from app.documents_loader import get_all_markdown_data
from app.retriever import get_retriever

document_data = get_all_markdown_data()

# Create the retriever
retriever = get_retriever(document_data)

# Create the RAG chain
rag_chain = create_rag_chain(retriever)

def get_response(prompt):
    """
    Generate a response from the RAG chain for a given prompt.
    
    Args:
        prompt (str): The input prompt for the chatbot.
    
    Returns:
        str: The chatbot's response.
    """
    abc = rag_chain.invoke({"input": prompt}, config={"configurable": {"session_id": "abc123"}})["answer"]
    return abc



