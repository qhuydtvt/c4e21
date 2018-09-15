def eval(x, y, sign):
    if sign == '+':
        result = x + y
    elif sign == '-':
        result = x - y
    elif sign == '*':
        result = x * y
    elif sign == '/':
        result = x / y
    return result

def generate_expression():
    x = randint(0, 10)
    y = randint(0, 10)
    sign = choice(['+', '-', '*', '/'])
    error = randint(-1, 1)
    result = eval(x, y, sign) + error
    return [x, y, sign, result]

def check_result(x, y, sign, result, answer):
    expected_result = eval(x, y, sign)
    if answer.lower() == 'y':
        if result == expected_result:
            return True
        else:
            return False
    else:
        if result != expected_result:
            return True
        else:
            return False

from random import randint, choice

x, y, sign, result = generate_expression()

print("* " * 10)
print("{0} {3} {1} = {2}".format(x, y, result, sign))
print("* " * 10)
answer = input("(Y/N)?")
if check_result(x, y, sign, result, answer):
    print("Yay")
else:
    print("Wrong :(")
