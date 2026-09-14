questions = [
    ("What keyword defines a function? ", "def"),
    ("What type stores key-value pairs? ", "dictionary"),
    ("What symbol starts a comment? ", "#"),
    ("What loop repeats while a condition is true? ", "while"),
    ("What value means no result? ", "none"),
]


def run_quiz(question_data):
    """Ask questions and return the score and percentage."""
    score = 0
    for question, expected in question_data:
        if input(question).strip().lower() == expected:
            score += 1
    return score, score / len(question_data) * 100


if __name__ == "__main__":
    print(run_quiz(questions))
