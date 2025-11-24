Quizora is an intelligent quiz-building application that generates high-quality multiple-choice questions (MCQs) from topics, text, PDFs, and even YouTube videos. Built with Python, NLP, and transformer-based models, Quizora supports both Single Mode and Multi Mode, making it suitable for students, teachers, and organizations.

Features
Single Mode – Generate a quiz from one specific topic
Multi Mode – Generate a combined quiz from multiple opics
PDF Upload – Extract text from a PDF and generate quiz questions
YouTube Link Input – Extract the transcript of a YouTube video and generate questions from it
AI-based MCQ generation using NLP and transformer models
Text-based quiz generation from pasted notes or articles
Difficulty selection: Easy, Medium, Hard
Customizable number of questions
Automatic distractor (incorrect option) generation
Answer key with explanations
Streamlit-based interactive UI

How It Works
User selects the mode (Single or Multi) or uploads a PDF/YouTube link.
Text is extracted and processed using NLP.
Key concepts are identified.
MCQs are generated using a question-generation model.
Distractors are created using semantic similarity.
The final quiz is displayed, along with answer keys and explanations.

Tech Stack
Python 3.x
Streamlit
pdfplumber or PyMuPDF for PDF text extraction
YouTube Transcript API (youtube-transcript-api)
spaCy / NLTK for NLP preprocessing

HuggingFace transformers for question generation

Scikit-learn for similarity scoring
