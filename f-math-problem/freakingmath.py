from random import *

def generate_quiz():
    # Hint: Return [x, y, op, r]
    return [0, 0, '+', 12]

def check_answer(x, y, op, r, user_choice):
    print("Check answer: ", user_choice)
    print(x, y, op, r)
    return False
