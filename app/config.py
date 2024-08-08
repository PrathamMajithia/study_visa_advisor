OPENAI_API_KEY = "___enter__here___"

# Chunking configuration
CHUNK_SIZE = 300
CHUNK_OVERLAP = 50

# Headers to split on
HEADERS_TO_SPLIT_ON = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

# Data folder path
DATA_FOLDER_PATH = "data/"

QUESTION_TEMPLATE = ( 
    "You are an assistant for question-answering tasks. Use the following pieces of context to answer the question at the end."
    "If you don't know the answer, just say that you don't know, don't try to make up an answer."
    "Use six sentences maximum and keep the answer as concise as possible."
    "Also remember, the questions are only regarding UK Study visas, any questions regarding any other countries are not welcome."
    "If the user greets you, greet them back."
    "\n\n"
    "{context}"
)

CONTEXT_TEMPLATE = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)
