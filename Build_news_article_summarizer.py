import os
from dotenv import load_dotenv
import requests
from newspaper import Article
from langchain.prompts.prompt import PromptTemplate
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
chatbot=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0,)
load_dotenv()
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
article_url = "https://www.artificialintelligence-news.com/2022/01/25/meta-claims-new-ai-supercomputer-will-set-records/"
def parsing_data(headers,article_url):

    session=requests.Session()
    try:
        responce = session.get(article_url,headers=headers, timeout=10)
        if responce.status_code == 200:
            article = Article(article_url)
            article.download()
            article.parse()
            return article
        
        else:
            print(f'Failed to fetch article. Status code: {responce.status_code}')
    except Exception as e:
        print(f'Error occurred while fetching article: {e}')
def chat_bot(article):
    article_text=article.text
    article_title=article.title
    templete="""You are a very good assistant that summarizes online articles.

    Here's the article you want to summarize.

    ==================
    Title: {article_title}

    {article_text}
    ==================

    Write a summary of the previous article.
    """
    prompt=PromptTemplate(input_types=["article_text","article_title"],template=templete)
    prompt.format(article_text=article_text,article_title=article_title)
    messages=[HumanMessage(content=prompt)]
    summary=chat_bot(messages)
    print(summary.content)
article=parsing_data(headers,article_url)
chat_bot(article)