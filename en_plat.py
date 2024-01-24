import streamlit as st
import login_page
from langchain_helper import get_few_shot_db_chain

def app():
    if(login_page.signed==True):

        st.title("Retail Store: Database enqiry 👕")

        question = st.text_input("Question: ")

        if question:
            chain = get_few_shot_db_chain()
            response = chain.run(question)

            st.header("Answer")
            st.write(response)
    else:
         st.subheader('Login First')


