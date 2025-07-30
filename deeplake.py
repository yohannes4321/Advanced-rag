from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings

from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from dotenv import load_dotenv
from langchain.vectorstores import DeepLake
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
import os


os.environ["GOOGLE_API_KEY"] = os.environ('google_api_key')
embeddings=GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-exp-03-07')
prompt=PromptTemplate(
  input_variables=['product'],
  template='what is good name for a companey{product}'
)

load_dotenv()



llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

conversation=ConversationChain(
    llm=llm,
    verbose=True,
    memory=ConversationBufferMemory()
)

# create our documents
texts = [
    "Napoleon Bonaparte was born in 15 August 1769",
    "Louis XIV was born in 5 September 1638"
]
text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
docs=text_splitter.create_documents(texts)
my_activeloop_org_id='johnalex'
my_activeloop_dataset_name='langchain_course_from_zero_to_hero'
dataset_path=f"hub://{my_activeloop_org_id}/{my_activeloop_dataset_name}"
db=DeepLake(dataset_path=dataset_path,embedding_function=embeddings)

db.add_documents(docs)
retrieval_qa=RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=db.as_retriever()
)
from langchain.agents import initialize_agent,Tool ,AgentType
tools=[
    Tool(
        name='Retrieval QA system',
        func=retrieval_qa,
        description='usefull for answering question'
    )
]
agent=initialize_agent(
    tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    Verbose=True
)
response=agent.run('when is Napoleone born')
print(response)
texts = [
    "Lady Gaga was born in 28 March 1986",
    "Michael Jeffrey Jordan was born in 17 February 1963"
]
db=DeepLake(dataset_path=dataset_path,embedding_function=embeddings)
text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
docs=text_splitter.create_documents(texts)
db.add_documents(docs)
from langchain.chains import RetrievalQA
retrival=RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=db.as_retriever()
)
tools=[
    Tool(
        name='retrival form db',
        func=retrival.run,
        description="usfull for answer from qa"
    )
]
agent=initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
os.environ['GOOGLE_CSE_ID']
os.environ['GOOGLE_API_KEY']
from langchain_core.tools import Tool
from langchain_google_community import GoogleSearchAPIWrapper


search=GoogleSearchAPIWrapper()
tools=[Tool(
    name='google_search',
    description='useful for when you need to search google to answer question about current events ',
    func=search.run
)]
agent=initialize_agent(
    tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True,max_iterations=6
)
responce=agent('What is the latest news about Mars')
print(responce['output'])
def summarize_text(query:str)-> str:
    return summarize_text.invoke({'query':query})

tools=[
    Tool(
        name='google_search',
        func=search.run,
        description='useful for finding infromation events searching google'
    ),
    Tool(
        name='Summerizer',
        func=summarize_text,
        description='useful for summerizing text'
    )
]
agent=initialize_agent(
    tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
resonse=agent("Details of President Ruto's Meeting With Abiy Ahmed in Ethiopia july 27 ? and then summarize the results")
print(resonse['output'])