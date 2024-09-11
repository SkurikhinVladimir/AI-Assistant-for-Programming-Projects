import streamlit as st

from file_handling import load_files_content
from streamlit_utils.sidebar import sidebar_function


def run_prompt_display_mode():
    sidebar_function()
    st.write("Displaying the full prompt without model invocation.")
    additional_prompt = load_files_content(st.session_state.return_select['checked'])
    prompt = st.text_input("Enter a message to display:")
    
    if prompt:
        full_text = additional_prompt + prompt
        st.text_area("Combined Output", value=full_text, height=200, max_chars=None, key="output_area")

run_prompt_display_mode()