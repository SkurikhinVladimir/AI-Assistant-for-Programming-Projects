import os
import streamlit as st

if not os.path.exists('projects'):
    os.makedirs('projects')

chat_mode = st.Page("views/chat_model.py", title="Chat Mode", icon="💬")
prompt_display_mode = st.Page("views/prompt_display_mode.py", title="Prompt display mode", icon="📄")
    
pg = st.navigation([chat_mode, prompt_display_mode])
    
pg.run()    