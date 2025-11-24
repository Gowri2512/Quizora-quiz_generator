import random

def generate_distractors(answer, num=3):
    words = ["system", "process", "data", "model", "analysis", "feature"]
    distractors = random.sample(words, num)
    return distractors
