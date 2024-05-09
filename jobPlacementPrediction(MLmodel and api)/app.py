import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st
import pickle

lg = pickle.load(open('placement.pkl','rb'))

# web app
img = Image.open('Job-Placement-Agency.jpg')
st.image(img,width=650)
st.title(" Building a Cutting-Edge Job Placement Prediction Model")

input_text = st.text_input("Enter all features")
if input_text:
    input_list = input_text.split(',')
    np_df = np.asarray(input_list,dtype=float)
    prediction = lg.predict(np_df.reshape(1,-1))

    if prediction[0] == 1:
        st.write("The individual above has completed their qualifications and secured a job.")
    else:
        st.write("The individual above has not secured a job")