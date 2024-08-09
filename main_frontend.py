import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the template and model
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer: 
"""

model = OllamaLLM(model='llama3')
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Function to handle conversation
def handle_conversation(context, user_input):
    result = chain.invoke({"context": context, "question": user_input})
    context += f'\nUser: {user_input}\nAI: {result}'
    return context, result

# Streamlit app
def main():
    st.title("AI Chatbot")
    st.write("Welcome to the AI chatbot. Type your message below and press Enter to chat.")

    if 'context' not in st.session_state:
        st.session_state.context = ''

    user_input = st.text_input("You: ", key="input")

    if st.button("Send"):
        if user_input:
            st.session_state.context, response = handle_conversation(st.session_state.context, user_input)
            st.write(f"Bot: {response}")

    st.write("Conversation History:")
    st.text_area("Context", st.session_state.context, height=300)

if __name__ == '__main__':
    main()
