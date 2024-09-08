import os
import google.generativeai as genai
os.environ['GOOGLE_API_KEY'] = "AIzaSyAy8zc0RgndnNyINoM2YAOBEgGpgf-_Onk"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')
from IPython.display import Markdown
model = genai.GenerativeModel('gemini-pro')
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-pro")
import json
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import json
from flask import Flask, request, jsonify









app = Flask(__name__)

first_prompt = ChatPromptTemplate.from_template(
    "Translate the following text to English:\n\n{input_text}"
)

chain_one = LLMChain(llm=llm, prompt=first_prompt, output_key="English_Review")


@app.route('/translate', methods=['POST'])
def translate_text():
    text = request.get_json()
    data=pd.DataFrame(text)
    text_to_translate = data["text"].values[0]
    if not text_to_translate:
        return jsonify({'error': 'No input text provided'}), 400
    
    result = chain_one.run(input_text=text_to_translate)
    return jsonify({'Translated text': result})

if __name__ == '__main__':
    app.run(debug=True)















