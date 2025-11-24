import streamlit as st
from utils.mcq_generator import generate_mcq

def run_single_mode():
    st.header("Single Mode Quiz Generation")
    topic = st.text_input("Enter Topic")

    if st.button("Generate Quiz"):
        mcqs = generate_mcq(topic)

        for i, q in enumerate(mcqs, start=1):
            st.subheader(f"Q{i}. {q['question']}")
            for opt in q["options"]:
                st.write(f"- {opt}")
            st.write(f"Answer: {q['answer']}")
