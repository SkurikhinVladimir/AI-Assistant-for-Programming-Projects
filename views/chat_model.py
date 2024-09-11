import streamlit as st
from langchain.schema import ChatMessage
from langchain_openai import ChatOpenAI

from callbacks.stream_handler import StreamHandler
from file_handling import load_files_content
from settings import settings
from streamlit_utils.sidebar import sidebar_function

openai_api_base = settings.api_base
model = settings.model_name
openai_api_key = settings.api_key


def initialize_messages():
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            ChatMessage(
                role="system",
                content=( 
                    "You are an AI assistant specialized in helping with programming projects. "
                    "You will be given multiple files as input, where each file includes its name and content. "
                    "Your task is to understand the structure and content of these files and provide helpful answers "
                    "to the user's questions. When the user asks a question, reference relevant parts of the code or "
                    "provide guidance on how to solve specific problems. Ensure that your responses are clear, concise, "
                    "and focused on the user's needs."
                )
            ),
        ]

def display_messages():
    for msg in st.session_state.messages:
        st.chat_message(msg.role).write(msg.content)

def handle_user_input():
    if prompt := st.chat_input():
        additional_prompt = load_files_content(st.session_state.return_select['checked'])
        full_prompt = additional_prompt + prompt
        st.chat_message("user").write(prompt)
        
        # Append user message to session state
        st.session_state.messages.append(ChatMessage(role="user", content=prompt))

        # In Chat Mode, make a request to the model
        with st.chat_message("assistant"):
            stream_handler = StreamHandler(st.empty())
            llm = ChatOpenAI(
                model=model,
                api_key=openai_api_key,
                openai_api_base=openai_api_base,
                streaming=True,
                callbacks=[stream_handler]
            )
            
            response = llm.invoke(st.session_state.messages + [ChatMessage(role="user", content=full_prompt)])
            st.session_state.messages.append(ChatMessage(role="assistant", content=response.content))

def clear_chat():
    with st.sidebar:
        if st.button('Clear Chat'):
            st.session_state.messages = [
                ChatMessage(
                    role="system",
                    content=( 
                        "You are an AI assistant specialized in helping with programming projects. "
                        "You will be given multiple files as input, where each file includes its name and content. "
                        "Your task is to understand the structure and content of these files and provide helpful answers "
                        "to the user's questions. When the user asks a question, reference relevant parts of the code or "
                        "provide guidance on how to solve specific problems. Ensure that your responses are clear, concise, "
                        "and focused on the user's needs."
                    )
                ),
            ]
            st.rerun()  # Rerun the script to refresh the chat display

def run_chat_mode():
    sidebar_function()
    clear_chat()
    initialize_messages()
    display_messages()
    handle_user_input()

run_chat_mode()
