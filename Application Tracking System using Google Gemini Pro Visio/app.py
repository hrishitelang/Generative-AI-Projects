from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import io
import base64
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        #Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode() # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    

## Streamlit App

st.set_page_config(page_title="ATS Resume EXpert")
st.header("ATS Tracking System")
input_text=st.text_area("Job description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...", type=["pdf"])

submit1 = st.button("Tell me about the Resume")
submit2 = st.button("How can I improvise on my skills?")
submit3 = st.button("Percentage match")

input_prompt1 = """
You are an experienced HR with Tech Experience in the field of Data Science, Full Stack web development
Big data engineering, Devops, Data Analyst, your task is to review the provided resume against the job description for these
profiles. Please share your professional evaluation on whether the candidate's profile aligns with the role
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements
"""

input_prompt2 = """
You are a technical human resource manager with expertise in data science, full stack, web development,
big data engineering, devops, data analyst, your role is to scrutinize the resume in  light of the job description provided.
Share your insights on the candidate's suitability for the role from an HR perspective
Additionally, offer advice on enhancing the candidate's skills and identify areas of improvement
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of Data Science, Full Stack web development
Big data engineering, Devops, Data Analyst and ATS functionality.
Your task is to evaluate the resume against the provided job description. give the percentage match if the resume matches 
the job description. The output should first come as percentage and then the missing keywords
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content,input_text)
        st.subheader("The Response is")
    else:
        st.write("Please upload the resume")
elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content,input_text)
        st.subheader("The Response is")
    else:
        st.write("Please upload the resume")







