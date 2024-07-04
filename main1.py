
import os
import streamlit as st

st.title("Resurent System")

from langchain_google_genai import ChatGoogleGenerativeAI
os.environ['GOOGLE_API_KEY'] = 'AIzaSyAABk46IgdfJ1t4eQ8IQep87m3mikNAzOU'
# llm = ChatGoogleGenerativeAI(model="gemini-pro")
# result = llm.invoke("Write a ballad about LangChain")
# print(result.content)
item=st.sidebar.selectbox('pick a item',('Indian','Mexican','Italian'))

