import streamlit as st
from utils.mcq_generator import generate_mcq

def run_multi_mode():
    st.header("Multi Mode Quiz Generation")
    topics = st.text_area("Enter multiple topics (comma separated)")

    if st.button("Generate Combined Quiz"):
        topics_list = topics.split(",")
        text = " ".join(topics_list)
        mcqs = generate_mcq(text)

        for i, q in enumerate(mcqs, start=1):
            st.subheader(f"Q{i}. {q['question']}")
            for opt in q["options"]:
                st.write(f"- {opt}")
            st.write(f"Answer: {q['answer']}")
