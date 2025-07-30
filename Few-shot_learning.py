# Quick introduction to large language model 
from langchain_core.prompts.few_shots import FewShotPromptTemplate
from langchain_core.prompts.prompt import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain 
examples = [
    {
        "query": "What's the weather like?",
        "answer": "It's raining cats and dogs, better bring an umbrella!"
    }, {
        "query": "How old are you?",
        "answer": "Age is just a number, but I'm timeless."
    }
]
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=google_api_key)

example_template="""
user :{query}
AI:{answer}
"""
example_prompt=PromptTemplate(
    input_variables=['query','answer'],
    template=example_template
)
prefix = """The following are excerpts from conversations with an AI
assistant. The assistant is known for its humor and wit, providing
entertaining and amusing responses to users' questions. Here are some
examples:
"""
suffix="""
User: {query}.
AI """ 
few_shot_prompt_template=FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=['query'],
    example_seprator="\n\n"
)
chain=few_shot_prompt_template|few_shot_template
chain.invoke("What's the meaning of life?")

tranlation_template="Translate the following text from  {source_languge} to {target_language} {text}"
translation_prompt=PromptTemplate(input_variables=['source_language','target_language','text'],template=tranlation_template)
translation_chain=LLMChain(llm=llm,prompt=translation_prompt)
source_language = "English"
target_language = "French"
text = "Your text here"

translation_chain.predict(source_language=source_language, target_language=target_language, text=text)