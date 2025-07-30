from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.prompts.few_shot import FewShotPromptTemplate
import os 
from dotenv import load_dotenv
load_dotenv()
os.environ['GOOGLE_API_KEY']
chat=ChatGoogleGenerativeAI(model='gemini-2.0-flash',temperature=0)
examples = [
    {
        "query": "What's the secret to happiness?",
        "answer": "Finding balance in life and learning to enjoy the small moments."
    }, {
        "query": "How can I become more productive?",
        "answer": "Try prioritizing tasks, setting goals, and maintaining a healthy work-life balance."
    }
]
example_prompt=""" 
'user':{query},
'AI':{answer}
"""
example_prompt_final=PromptTemplate(input_variables=['query','answer'],template=example_prompt)
prefix="you are life coach chatbot the give advice for clients for this question  "
suffix="question {question}" \
"AI  "
question='what to be good communicator  and to be leader for all but you people say you are selfish who thing for himself only ' \
'and you make frendship and to make normal with person'

few_shot=FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt_final,
    prefix=prefix,
    suffix=suffix,
    input_variables=['question'],
    example_separator="\n"
)
chain=few_shot|chat
result=chain.invoke({'question':question})
print(result.content)