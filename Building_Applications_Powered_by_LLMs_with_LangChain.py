from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.environ('google_api_key')
llm=GoogleGenerativeAI(model='gemini-2.0-flash')
from langchain_core.prompts import (ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate)
os.environ["GOOGLE_API_KEY"] =os.getenv("google_api_key")

template="You are an assistant that helps users find information about movies."
system_message_prompt=SystemMessagePromptTemplate.from_template(template)
human_template="Find information about the movie {movie_title}."
human_prompt=HumanMessagePromptTemplate.from_template(human_template)
chat_prompt=ChatPromptTemplate.from_messages([system_message_prompt,human_template])
responce=llm.invoke(chat_prompt.format_prompt(movie_title="Inception").to_messages())
print(responce)