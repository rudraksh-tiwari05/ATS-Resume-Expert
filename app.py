from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import io
import base64
from PIL import Image
import pdf2image
import google.generativeai as genai

# Configure Generative AI API
genai.configure(api_key=os.getenv('Google_api_key'))

def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_text, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                'mime_type': 'image/jpeg',
                'data': base64.b64encode(img_byte_arr).decode(),
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError('No File Uploaded')

# Streamlit UI
st.set_page_config(page_title='ATS Resume Expert')
st.header('ATS Tracking System')
input_text = st.text_area('Job Description', key='input')
uploaded_file = st.file_uploader('Upload your Resume (PDF)...', type=['pdf'])

if uploaded_file is not None:
    st.write('PDF Uploaded Successfully')

submit1 = st.button('Tell me about the resume')
submit2 = st.button('How can I improve my skills')
submit3 = st.button('Percentage match')

input_prompt1 = '''You are an experienced HR with Tech Experience in the field of data science, full stack, web development,
Big Data engineering, DEVOPS, Data Analyst. Your task is to review the provided resume against the job description for these profiles.
Please share your professional evaluation on whether the candidate's profile aligns with the role, highlighting the strengths and weaknesses
of the applicant in relation to the specified job role.'''

input_prompt2 = '''You are an experienced HR with Tech Experience in the field of data science, full stack, web development,
Big Data engineering, DEVOPS, Data Analyst. Your task is to review the provided resume against the job description for these profiles.
Please share your professional evaluation on whether the candidate's profile aligns with the role, highlighting the strengths and weaknesses
of the applicant in relation to the specified job role.'''

input_prompt3 = '''You are an experienced HR with Tech Experience in the field of data science, full stack, web development,
Big Data engineering, DEVOPS, Data Analyst. Your task is to evaluate the percentage match of the provided resume against the job description
for these profiles. Please provide the percentage match and any key observations.'''

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_prompt1)
        st.subheader(response)
    else:
        st.write('Please upload the resume')

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_prompt2)
        st.subheader(response)
    else:
        st.write('Please upload the resume')

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_prompt3)
        st.subheader(response)
    else:
        st.write('Please upload the resume')
