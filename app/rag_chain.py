from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY, QUESTION_TEMPLATE, CONTEXT_TEMPLATE
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    """
    Retrieve or create a chat message history for a given session.
    
    Args:
        session_id (str): The session identifier.
    
    Returns:
        BaseChatMessageHistory: The chat message history for the session.
    """
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

def create_rag_chain(retriever):
    """
    Create a Retrieval-Augmented Generation (RAG) chain.
    
    Args:
        retriever (Retriever): The retriever object.
    
    Returns:
        RunnableWithMessageHistory: The RAG chain configured for conversational AI.
    """
    llm = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=OPENAI_API_KEY)
    # Contextualize question prompt
    contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", CONTEXT_TEMPLATE),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
    )
    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt
    )

    # Question-answer chain prompt
    qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", QUESTION_TEMPLATE),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
    )
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

    # Combine the retriever and question-answer chain into a RAG chain
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer",
    )
    return conversational_rag_chain