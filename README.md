Building Applications Powered by LLMs with LangChain
Introduction
LangChain is designed to assist developers in building end-to-end applications using language models. It offers an array of tools, components, and interfaces that simplify the process of creating applications powered by large language models and chat models. LangChain streamlines managing interactions with LLMs, chaining together multiple components, and integrating additional resources, such as APIs and databases. Having gained a foundational understanding of the library in previous lesson, let's now explore various examples of utilizing prompts to accomplish multiple tasks.

Prompt use case:
A key feature of LangChain is its support for prompts, which encompasses prompt management, prompt optimization, and a generic interface for all LLMs. The framework also provides common utilities for working with LLMs.

ChatPromptTemplate is used to create a structured conversation with the AI model, making it easier to manage the flow and content of the conversation. In LangChain, message prompt templates are used to construct and work with prompts, allowing us to exploit the underlying chat model's potential fully.

System and Human prompts differ in their roles and purposes when interacting with chat models. SystemMessagePromptTemplate provides initial instructions, context, or data for the AI model, while HumanMessagePromptTemplate are messages from the user that the AI model responds to.

To illustrate it, let’s create a chat-based assistant that helps users find information about movies. Ensure your OpenAI key is stored in environment variables using the “OPENAI_API_KEY” name. Remember to install the required packages with the following command: 


Exploring the World of Language Models: LLMs vs Chat Models
 

Introduction
Large Language Models have made significant advancements in the field of Natural Language Processing (NLP), enabling AI systems to understand and generate human-like text. ChatGPT is a popular language model based on Transformers architecture, enabling it to understand long texts and figure out how words or ideas are connected. It's great at making predictions about language and relationships between words.

LLMs and Chat Models are two types of models in LangChain, serving different purposes in natural language processing tasks. This lesson will examine the differences between LLMs and Chat Models, their unique use cases, and how they are implemented within LangChain. 

Understanding LLMs and Chat Models
LLMs
LLMs, such as GPT-3, Bloom, PaLM, and Aurora genAI, take a text string as input and return a text string as output. They are trained on language modeling tasks and can generate human-like text, perform complex reasoning, and even write code. LLMs are powerful and flexible, capable of generating text for a wide range of tasks. However, they can sometimes produce incorrect or nonsensical answers, and their API is less structured compared to Chat Models.

Pre-training these models involves presenting large-scale corpora to them and allowing the network to predict the next word, which results in learning the relationships between words. This learning process enables LLMs to generate high-quality text, which can be applied to an array of applications, such as automatic form-filling and predictive text on smartphones.

Most of these models are trained on general purpose training dataset, while others are trained on a mix of general and domain-specific data, such as Intel Aurora genAI, which is trained on general text, scientific texts, scientific data, and codes related to the domain. The goal of domain specific LLMs is to increase the performance on a particularly domain, while still being able to solve the majority of tasks that general LLM can manage.

LLMs have the potential to infiltrate various aspects of human life, including the arts, sciences, and law. With continued development, LLMs will become increasingly integrated into our educational, personal, and professional lives, making them an essential technology to master.

You can follow these steps to use a large language model (LLM) like GPT-3 in LangChain. Import the OpenAICopy wrapper from the langchain.llmsCopy module and Initialize it with the desired model name and any additional arguments. For example, set a high temperature for more random outputs. Then, create a PromptTemplateCopy to format the input for the model. Lastly, define a pipeCopy to combine the model and prompt. Run the chain with the desired input using .run()Copy. As mentioned before, remember to set your OpenAI key saved in the “OPENAI_API_KEY” environment variable before running the following codes. Remember to install the required packages with the following command: 

Copy
pip install -qU langchain-openai
pip install -qU langchain-communityCopy
Copy
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# Before executing the following code, make sure to have
# your OpenAI key saved in the “OPENAI_API_KEY” environment variable.
llm = ChatOpenAI(model_name = "gpt-4o-mini", temperature=0)

prompt = PromptTemplate(
  input_variables=["product"],
  template="What is a good name for a company that makes {product}?",
)

chain = prompt | llm

print( chain.invoke("wireless headphones") )Copy
The sample code.
Copy
Wireless Audio SolutionsCopy
The output.
Here, the input for the chain is the string "wireless headphones". The chain processes the input and generates a result based on the product name.

Chat Models
Chat Models are the most popular models in LangChain, such as ChatGPT that can incorporate GPT-3 or GPT-4 at its core. They have gained significant attention due to their ability to learn from human feedback and their user-friendly chat interface.

Chat Models, such as ChatGPT, take a list of messages as input and return an AIMessageCopy. They typically use LLMs as their underlying technology, but their APIs are more structured. Chat Models are designed to remember previous exchanges with the user in a session and use that context to generate more relevant responses. They also benefit from reinforcement learning from human feedback, which helps improve their responses. However, they may still have limitations in reasoning and require careful handling to avoid generating inappropriate content.

API Differences in LangChain

Chat Message Types

In LangChain, three main types of messages are used when interacting with chat models: SystemMessageCopy, HumanMessageCopy, and AIMessageCopy.

SystemMessage: These messages provide initial instructions, context, or data for the AI model. They set the objectives the AI should follow and can help in controlling the AI's behavior. System messages are not user inputs but rather guidelines for the AI to operate within.

HumanMessage: These messages come from the user and represent their input to the AI model. The AI model is expected to respond to these messages. In LangChain, you can customize the human prefix (e.g., "User") in the conversation summary to change how the human input is represented.

AIMessage: These messages are sent from the AI's perspective as it interacts with the human user. They represent the AI's responses to human input. Like HumanMessage, you can also customize the AI prefix (e.g., "AI Assistant" or "AI") in the conversation summary to change how the AI's responses are represented.

An example of using ChatOpenAI with a HumanMessage: In this section, we are trying to use the LangChain library to create a chatbot that can translate an English sentence into French. This particular use case goes beyond what we covered in the previous lesson. We'll be employing multiple message types to differentiate between users' queries and system instructions instead of relying on a single prompt. This approach will enhance the model's comprehension of the given requirements.

First, we create a list of messages, starting with a SystemMessageCopy that sets the context for the chatbot, informing it that its role is to be a helpful assistant translating English to French. We then follow it with a HumanMessageCopy containing the user’s query, like an English sentence to be translated.

Copy
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

chat = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

messages = [
	SystemMessage(content="You are a helpful assistant that translates English to French."),
	HumanMessage(content="Translate the following sentence: I love programming.")
]

chat(messages).contentCopy
The sample code.
Copy
AIMessage(content="J'aime la programmation.", additional_kwargs={}, example=False)Copy
The output.
As you can see, we pass the list of messages to the chatbot using the chat()Copy function. The chatbot processes the input messages, considers the context provided by the system message, and then translates the given English sentence into French. 

💡
SystemMessageCopy represents the messages generated by the system that wants to use the model, which could include instructions, notifications, or error messages. These messages are not generated by the human user or the AI chatbot but are instead produced by the underlying system to provide context, guidance, or status updates.
Using the generate method, you can also generate completions for multiple sets of messages. Each batch of messages can have its own SystemMessageCopy and will perform independently. The following code shows the first set of messages translate the sentences from English to French, while the second ones do the opposite.

Copy
batch_messages = [
  [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="Translate the following sentence: I love programming.")
  ],
  [
    SystemMessage(content="You are a helpful assistant that translates French to English."),
    HumanMessage(content="Translate the following sentence: J'aime la programmation.")
  ],
]
print( chat.generate(batch_messages) )Copy
The sample code.
Copy
LLMResult(generations=[[ChatGeneration(text="J'aime la programmation.", generation_info=None, message=AIMessage(content="J'aime la programmation.", additional_kwargs={}, example=False))], [ChatGeneration(text='I love programming.', generation_info=None, message=AIMessage(content='I love programming.', additional_kwargs={}, example=False))]], llm_output={'token_usage': {'prompt_tokens': 65, 'completion_tokens': 11, 'total_tokens': 76}, 'model_name': 'gpt-4'})Copy
The output.
As a comparison, here's what LLM and Chat Model APIs look like in LangChain.

Copy
llm_output:  {'product': 'Translate the following text from English to French: Hello, how are you?', 'text': '\n\nBonjour, comment allez-vous?'}

chat_output:  content='Bonjour, comment ça va ?' additional_kwargs={} example=FalseCopy
The output.
Conclusion
LLMs and Chat Models each have their advantages and disadvantages. LLMs are powerful and flexible, capable of generating text for a wide range of tasks. However, their API is less structured compared to Chat Models.

On the other hand, Chat Models offer a more structured API and are better suited for conversational tasks. Also, they can remember previous exchanges with the user, making them more suitable for engaging in meaningful conversations. Additionally, they benefit from reinforcement learning from human feedback, which helps improve their responses. They still have some limitations in reasoning and may require careful handling to avoid hallucinations and generating inappropriate content.

In the next lesson we’ll see how GPT-4 and ChatGPT can be used for context-aware chat applications via APIs.

