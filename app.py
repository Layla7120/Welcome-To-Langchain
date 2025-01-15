from datetime import datetime

import openai
import streamlit as st

st.set_page_config(
    page_title="FullStackGPT Home",
    page_icon="🤖"
)

st. subheader("2025-01-15")

st.markdown(
    """
    # Streamlit is 🔥
    
    ## 📃 [DocumentGPT](/DocumentGPT)
    """
)

with st.sidebar:
    st.title("OpenAI API KEY")
    API_KEY = st.text_input("Use your API KEY")

    if API_KEY:
        openai.api_key = API_KEY
    st.title("🔗 Github Repo")
    st.markdown("[![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/Layla7120/Welcome-To-Langchain)")

