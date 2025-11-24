import streamlit as st
from modes.single_mode import run_single_mode
from modes.multi_mode import run_multi_mode
from processors.pdf_processor import process_pdf
from processors.youtube_processor import process_youtube

st.set_page_config(page_title="Quizora", layout="wide")

st.title("Quizora – AI Quiz Generator")

mode = st.sidebar.selectbox(
    "Select Mode",
    ["Single Mode", "Multi Mode", "PDF Upload", "YouTube Video"]
)

if mode == "Single Mode":
    run_single_mode()

elif mode == "Multi Mode":
    run_multi_mode()

elif mode == "PDF Upload":
    st.header("Generate Quiz from PDF")
    pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
    if pdf_file:
        text = process_pdf(pdf_file)
        st.write("Extracted Text:")
        st.write(text)

elif mode == "YouTube Video":
    st.header("Generate Quiz from YouTube Video")
    url = st.text_input("Enter YouTube URL")
    if url:
        text = process_youtube(url)
        st.write("Extracted Transcript:")
        st.write(text)
