from langchain_text_splitters import MarkdownHeaderTextSplitter
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config import DATA_FOLDER_PATH
from app.config import HEADERS_TO_SPLIT_ON, CHUNK_SIZE, CHUNK_OVERLAP

def read_markdown_file(file_path):
    """
    Read the contents of a markdown file.
    
    Args:
        file_path (str): The path to the markdown file.
    
    Returns:
        str: The contents of the file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def get_markdown_files(data_folder_path):
    """
    Retrieve all markdown file paths in the specified folder.
    
    Args:
        data_folder_path (str): The path to the folder containing markdown files.
    
    Returns:
        list: A list of file paths to markdown files.
    """
    return [os.path.join(data_folder_path, file) for file in os.listdir(data_folder_path) if file.endswith(".md")]

def split_markdown_content(markdown_content):
    """
    Split markdown content into sections based on headers.
    
    Args:
        markdown_content (str): The markdown content to split.
    
    Returns:
        list: A list of split sections of the markdown content.
    """
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=HEADERS_TO_SPLIT_ON, strip_headers=False)
    splits = markdown_splitter.split_text(markdown_content)
    return splits

def split_documents(docs):
    """
    Further split documents into smaller chunks.
    
    Args:
        docs (list): List of document sections.
    
    Returns:
        list: A list of smaller document chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
    )
    return text_splitter.split_documents(docs)

def get_all_markdown_data():
    """
    Load and split all markdown data from the specified data folder.
    
    Returns:
        list: A list of document chunks from all markdown files.
    """
    markdown_files = get_markdown_files(DATA_FOLDER_PATH)
    all_splits = []

    for file_path in markdown_files:
        markdown_content = read_markdown_file(file_path)

        # Split the content into sections
        splits = split_markdown_content(markdown_content)

        # Further split sections into smaller chunks
        splits = split_documents(splits)
        all_splits.extend(splits)
    return all_splits