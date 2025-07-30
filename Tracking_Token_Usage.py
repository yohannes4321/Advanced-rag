from langchain.chat_models import ChatOpenAI
from langchain_community.callbacks import get_openai_callback
llm=ChatOpenAI(model='gpt-4o-mini',n=2)
with get_openai_callback() as cb:
    result=llm.invoke('tell me a joke')
    print(cb)