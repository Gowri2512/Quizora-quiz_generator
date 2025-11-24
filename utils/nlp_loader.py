from transformers import T5ForConditionalGeneration, T5Tokenizer

def load_qg_model():
    model = T5ForConditionalGeneration.from_pretrained("iarfmoose/t5-base-question-generator")
    tokenizer = T5Tokenizer.from_pretrained("t5-base")
    return model, tokenizer
