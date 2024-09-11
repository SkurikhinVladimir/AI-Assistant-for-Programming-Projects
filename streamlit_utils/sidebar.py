import os

import streamlit as st

from file_handling import get_directory_tree
from streamlit_tree_select import tree_select


def sidebar_function():
    with st.sidebar:
        if 'return_select' not in st.session_state:
            st.session_state.return_select = {"checked": [], "expanded": []}
        if 'selected_folder' not in st.session_state:
            st.session_state.selected_folder = None
        files = os.listdir("projects")

        default_folder = st.session_state.selected_folder if st.session_state.selected_folder in files else files[0]
        selected_folder = st.selectbox("Выберите папку:", files, index=files.index(default_folder))

        if selected_folder:
            # Update the selected folder in the session state
            st.session_state.selected_folder = selected_folder
            directory_path = os.path.join("projects", selected_folder)
            nodes = get_directory_tree(directory_path, exclude_files="__pycache__")

            return_select = tree_select(
                nodes, 
                checked=st.session_state.return_select["checked"],
                expanded=st.session_state.return_select['expanded']
            )
            
            if st.session_state.return_select != return_select:
                st.session_state.return_select = return_select
                st.rerun()
