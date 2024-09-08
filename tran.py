import streamlit as st
import pandas as pd
import os
import google.generativeai as genai
os.environ['GOOGLE_API_KEY'] = "AIzaSyAy8zc0RgndnNyINoM2YAOBEgGpgf-_Onk"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')
from IPython.display import Markdown
model = genai.GenerativeModel('gemini-pro')
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-pro")
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain





first_prompt = ChatPromptTemplate.from_template(
    "Translate the following text to English:\n\n{input_text}"
)

chain_one = LLMChain(llm=llm, prompt=first_prompt, output_key="English_Review")




st.title("Text Translation App")

text_to_translate = st.text_area("Enter text to translate:")

if st.button("Translate"):
    if not text_to_translate:
        st.error("No input text provided")
    else:
        result = chain_one.run(input_text=text_to_translate)
        st.write("Translated text:", result)