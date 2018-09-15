x = float(input("x = "))
sign = str(input("Operation(+,-,*,/): "))
y = float(input("y = "))
result = None

def eval():
    if sign == '+':
        result = x + y
    elif sign == '-':
        result = x - y
    elif sign == '*':
        result = x * y
    elif sign == '/':
        result = x / y
    return result

print("* " * 10)
print("{0} {1} {2} = {3}".format(x, sign, y, eval()))
print("* " * 10)
