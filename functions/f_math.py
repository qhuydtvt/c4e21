from random import randint, choice

x = randint(0, 10)
y = randint(0, 10)
error = randint(-1, 1)
result = x + y + error
print("* " * 10)
print("{0} + {1} = {2}".format(x, y, result))
print("* " * 10)
answer = input("(Y/N)? ").lower()
expected_result = x + y
if answer.lower() == 'y':
    if result == expected_result:
        print("Yay")
    else:
        print("You're wrong")
else:
    if result != expected_result:
        print("Yay")
    else:
        print("You're wrong")
