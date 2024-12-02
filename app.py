# This Python script uses Streamlit to create a web application that helps users analyze their resumes against a job description using Google Gemini.
# This project is designed to help users improve their resumes by providing feedback on how well their resumes align with a given job description.
import streamlit as st
import PyPDF2 as pdf
import google.generativeai as genai

def get_gemini_response(input):
    """
    This function takes user input and sends it to the Google Gemini model for processing.
    It then returns the response from the model as text.
    """
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    """
    This function takes an uploaded PDF file and extracts the text from it.
    It then returns the extracted text as a string.
    """
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

def process_button(input_prompt):
    """
    This function handles the logic for processing the user's input and displaying the response.
    It checks if a file has been uploaded and then sends the input prompt to the Gemini model.
    Finally, it displays the response from the model.
    """
    if uploaded_file is not None:
        genai.configure(api_key=api_secret_key)
        response=get_gemini_response(input_prompt)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

## Streamlit App

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
# API Key Input (Password Field)
api_secret_key = st.text_input("Enter your Google Generative AI API key", type="password")

jd_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)",type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("How Can I Improve my profile")

if submit1:
    if uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)
        input_prompt1 = f"You are a highly skilled ATS (Applicant Tracking System) simulator with advanced knowledge of ATS functionality. Your task is to analyze the provided resume against the given job description. Provide:\n1. A percentage match indicating the alignment between the resume and job requirements.\n2. A detailed evaluation of how well the candidate's profile aligns with the role, highlighting specific strengths and weaknesses in relation to the job requirements. Resume:{resume_text}\nJob Description:{jd_text}"
        process_button(input_prompt1)

if submit2:
    if uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)
        input_prompt2 = f"You are a Hiring Manager evaluating a candidate's resume against a specific job description. Your task is to provide a professional assessment focused solely on actionable improvements needed for the candidate's profile to align more closely with the job requirements. Avoid discussing the candidate's strengths or weaknesses. Resume:{resume_text}\nJob Description:{jd_text}"
        process_button(input_prompt2)
