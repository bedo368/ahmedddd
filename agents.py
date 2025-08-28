from crewai import Agent 
from crewai import LLM
from config import OPEN_ROUTER_API_KEY

# llm = LLM(model = "deepseek-r1:1.5b", base_url="http://localhost:11434")   **this is ollama but he is slowly in runing so i uesd openrouter

llm = LLM(model="openrouter/deepseek/deepseek-r1",
         temperature = 0,
         api_key=OPEN_ROUTER_API_KEY
         )


def create_router_agent():
    return Agent(
        role='Router',
        goal='Route user query to either vectorstore or web search based on content relevance',
        backstory=(
            "you are an expert at deterimining whether a query can be answered using the"
            "information stored in our vector database , or requires a web search. "
            "you understand that the vector database contains comprehansive knowledge base "
            "you make routing decisions based on the semantic meaning of querys rather then just keyword matching."
        ),
        verbose= True,
        allow_delegation= False ,
        llm=llm,
    
    )


def create_retriever_agent():
    return Agent(
        role="Retriever",
        goal="Use the information retrieved form the vectorstore to answer the user query",
        backstory=(
            "You are an assistant for query-answering tasks."
            "Use the information present in the retrieved context to answer the user query" 
            "You have to provide a clear concise answer "
        ),
        verbose= True,
        allow_delegation= False, 
        llm=llm,
    )


def create_grader_agent():
    return Agent(
        role= "Answer Grader",
        goal='Filter out erroneous retrievals',
        backstory=(
            "You are a grader assessing relevance of a retrieved document to a user query. "
            "If the document contains keywords related to the user query , grade it as relevant "
            "it does not need to be a stringent test . You have to make sure that the answer is relevant to the query. "
        ),
        verbose= True ,
        allow_delegation=False , 
        llm=llm,
    )


def create_hallucination_grader():
    return Agent(
        role="Hallucination Grader",
        goal="Filter out hallucination",
        backstory=(
            "You are a hallucination grader assessing whether an answer is grounded in / supported by a set of facts."
            "Make sure you meticulously review the answer and check if the response provided is in alignmnet with the question asked"
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )
 

def create_answer_grader():
    return Agent(
        role="Answer Grader",
        goal="Filter out hallucination from the answer.",
        backstory=(
            "You are a grader assessing whether an answer is useful to resolve a question."
            "Make sure you meticulously review the answer and check if it makes sense for the question asked"
            "If the answer is relevant generate a clear and concise response."
            "If the answer gnerated is not relevant then perform a websearch using 'web_search_tool'"
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )  


