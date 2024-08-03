from dotenv import load_dotenv

load_dotenv()

import streamlit as st 
import io 
import base64
import os 
from PIL import Image 
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, propmt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content[0], propmt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
    
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = images[0]

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr,format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [

            {
                "mime_type" : "image/jpeg",
                "data" : base64.b64encode(img_byte_arr).decode()
            }

        ]

        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")


# streamlit app

st.set_page_config(page_title="Resume Scanning and Shortlisting AI for Scala/Spark", page_icon=":mag_right::mortar_board:")
# st.header("Scala/Spark Resume Scanner AI", divider="gray")
st.markdown("## :mag_right::mortar_board: Scala/Spark Resume Scanner AI")
input_text = st.text_area("Job Description: ",key="input")
uploaded_file = st.file_uploader("Upload your resume(PDF)...",type=["pdf"])

if uploaded_file is not None:
    st.write("file uploaded successfully")

submit1 = st.button("Summarize Candidate Profile")

submit2 = st.button("Check Percentage Match")

input_prompt1 = """ 

You are an highly experienced Technical Human Resource Manager with expertise in Scala and Spark,your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
Score each metric on the range of 1-10.

Finally, give me the final verdict wether the candidate should be selected or not.
"""

input_prompt2 = """
You are an highly skilled ATS (Applicant Tracking System) scanner with a deep understanding of data engineering, Scala, Spark and ATS functionality, 
your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches the job description. 
First the output should come as percentage match and then keywords missing, then detailed evaluation with verdict and last final thoughts.

Finally, give me a set of 5 advanced questions specific to this resume= that can be asked to the candidate to get an evaluation done by the interviewer.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)

        st.subheader("The Output of the evaluation (1) is:")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)

        st.subheader("The Output of the evaluation (2) is:")
        st.write(response)
    else:
        st.write("Please upload the resume in pdf format.")