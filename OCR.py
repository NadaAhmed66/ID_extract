import streamlit as st
import numpy as np
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.title('Document Scanner Application')

def extract_text(img):
    text=pytesseract.image_to_string(img)
    return text 

upload=st.file_uploader("please , upload an image...",type=['png','jpg','jpeg','WEBP'])

if upload is not None:
    img = Image.open(upload)
    img = np.array(img)
    st.image(img, caption='Uploaded image')

    text = extract_text(img)
    text_list = text.splitlines()
   

    
    st.write('🏛️ Organization Name : ',text_list[7],text_list[8]) 
    st.write('📅',text_list[4],text_list[5])
    st.write('👤',text_list[10],text_list[11]) 
    st.write('🎓',text_list[13],text_list[14])
    st.write('📘',text_list[16],text_list[17])
    st.write('🎂',text_list[19],text_list[20])
