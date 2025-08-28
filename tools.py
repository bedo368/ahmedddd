from pathlib import Path
from crewai.tools import BaseTool 
from crewai_tools.tools.file_read_tool import FileReadTool
from crewai.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from config import GROQ_API_KEY 


def create_pdf_tool(pdf_path):
    """
    A tool to read the content of a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        FileReadTool: A configured file reading tool instance.
    """
    return FileReadTool(file_path=pdf_path)


@tool 
def web_search_tool(query : str) -> str: 
    """
    Web Search Tool.

    Args : 
        query (str): the search query .

    returns : 
        str: The search results as text . 

    """
    web_search_tool = TavilySearchResults( K = 3 )
    return web_search_tool.run(query)
