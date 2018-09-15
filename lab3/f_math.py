# 1. Generate expression
from random import randint, choice
from calc import calculate

x = randint(0, 9)
y = randint(0, 9)
op = choice(["+", "-", "*", "/"])
error = randint(-1, 1)

r = calculate(x, y, op) + error

print(x, op, y, "=", r)

# 2. Ask user
user_answer = input("(Y/N)? ").upper()

# 3. Print result
if calculate(x, y, op) == r:
  if user_answer == "Y":
    print("Yay")
  elif user_answer == "N":
    print("Nah")
else:
  if user_answer == "Y":
    print("Nah")
  elif user_answer == "N":
    print("Yay")