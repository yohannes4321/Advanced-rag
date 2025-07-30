from langchain_core.prompts.prompt import PromptTemplate
import os 
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains.summarize import load_summarize_chain
os.environ["GOOGLE_API_KEY"] =os.getenv("google_api_key")
llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash')
document_loader=PyPDFLoader(file_path='CV (4).pdf')
document=document_loader.load()
summerize_chain=load_summarize_chain(llm)
print(summerize_chain(document['page_content']))