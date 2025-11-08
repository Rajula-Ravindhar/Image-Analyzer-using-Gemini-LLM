import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image


load_dotenv()
api_key=os.getenv('Gemini_ApiKey')
genai.configure(api_key=api_key)

st.header('Image Analytics')
uploaded_file=st.file_uploader('Upload an image',type=['png','jpg','jpeg','webp'])
if uploaded_file is not None:
    st.image(Image.open(uploaded_file))
 
prompt=st.text_input('Enter the prompt')

if st.button('Get Response',type='primary'):
    img=Image.open(uploaded_file)
    model=genai.GenerativeModel(model_name='models/gemini-2.5-flash')
    response=model.generate_content([prompt,img])
    st.markdown(response.text)