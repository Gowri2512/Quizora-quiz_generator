from utils.text_cleaner import clean_text
from utils.nlp_loader import load_qg_model
from utils.distractor_generator import generate_distractors

def generate_mcq(text, num_questions=5):
    text = clean_text(text)
    model, tokenizer = load_qg_model()

    questions = []
    for _ in range(num_questions):
        inputs = tokenizer.encode("generate question: " + text, return_tensors="pt")
        outputs = model.generate(inputs, max_length=64, num_return_sequences=1)

        question = tokenizer.decode(outputs[0], skip_special_tokens=True)
        answer = "Sample Answer"

        mcq = {
            "question": question,
            "options": generate_distractors(answer) + [answer],
            "answer": answer
        }

        questions.append(mcq)

    return questions
