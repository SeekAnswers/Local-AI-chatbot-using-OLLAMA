#To make this work, you would need to download and install Ollama to your PC and install the LLAMA3 model
#Then in terminal use ollama pull llama3 and the llama3 model will be downloaded
#Then you can use it and the code would work 

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer: 
"""

model = OllamaLLM(model='llama3')
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

#To be able to handle conversations and have a conversation history
def handle_conversation():
    context = ''
    print("Welcome to the AI chatbot, type 'exit' to quit.")
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'exit':
            break
        
        
        result = chain.invoke({"context": context, "question": user_input})
        print('Bot: ', result)
        context += f'\nUser: {user_input}\nAI: {result}'


if __name__ == '__main__':
    handle_conversation()
