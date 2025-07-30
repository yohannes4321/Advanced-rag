from langchain_core.prompts.few_shot import FewShotPromptTemplate

from langchain_core.prompts.prompt import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] 
llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash')
examples = [
    {"color": "red", "emotion": "passion"},
    {"color": "blue", "emotion": "serenity"},
    {"color": "green", "emotion": "tranquility"},
]
prompt_template="""
Color :{color},
Emotion:{emotion}
"""
example_format_promopt=PromptTemplate(input_variables=['color','emotion'],template=prompt_template)
few_shot_prompt=FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_format_promopt,
    prefix="\n\nsome example of collor emotion associated with them\n\n",
    suffix="\n\n now given a new color the emotion associated with them {input}\n\n ",
    input_variables=['question'],
    example_separator="\n"
)

chain=few_shot_prompt| llm
responce=chain.invoke({'input':'black'})
print(responce.content)