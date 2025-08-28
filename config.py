import os 
from dotenv import load_dotenv
load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
LLM_MODEL_PATH = os.getenv("LLM_MODEL_PATH")
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
OPEN_ROUTER_API_KEY = os.getenv('OPEN_ROUTER_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# ALL CLEAR 