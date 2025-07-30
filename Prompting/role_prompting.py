from langchain_core.prompts.prompt import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv() 

os.environ["GOOGLE_API_KEY"]
llm=GoogleGenerativeAI(model='gemini-2.0-flash',temperature=0)
template="""as a stursistic robot band conductor i need you to help me to come up with song title 
what is cool song title for song about {theme} in the year {year} """
prompt=PromptTemplate(
    input_variables=['theme','year'],
    template=template
)
chain=prompt|llm
input_data = {"theme": "interstellar travel", "year": "3030"}
responce=chain.invoke(input_data)
print(responce)