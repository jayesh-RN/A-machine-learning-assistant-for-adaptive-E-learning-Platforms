from flask import Flask,request,jsonify,render_template
import pickle
from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

app = Flask(__name__)



@app.route("/")
def hello():
    return jsonify({'message': 'hi'})



# @app.route("/ask",methods=['POST'])
# def fun():
#     question = request.json['question']
    
#     genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#     model=genai.GenerativeModel("gemini-pro") 
#     chat = model.start_chat(history=[])
#     response=chat.send_message(question)
#     print("\n")
#     print("\n")
#     print("\n")
#     print("\n")
    
#     candidates = response.candidates

#     # Assuming you want to access the first candidate
#     first_candidate = candidates[0]

#     # Accessing the content of the first candidate
#     content = first_candidate.content

#     # Accessing the parts of the content
#     parts = content.parts

#     # Assuming you want to access the text from the first part
#     first_part_text = parts[0].text

#     # print(first_part_text) 
    
#     text = first_part_text.replace('*', '')

#     # Remove newline characters ('\n')
#     text = text.replace('\n', '')
#     text = text.replace('  ', '')

#     # print(text)
    
    
#     print("\n")
#     print("\n")
#     print("\n")
#     print("\n")
#     return jsonify(({'response': text}))


    
if __name__ == '__main__':
    app.run(debug=True)