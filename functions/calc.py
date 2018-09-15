x = int(input("x = "))
op = input("Operation(+,-,*,/): ")
y = int(input("y = "))

if op == '+':
    result = x + y
elif op == '-':
    result = x - y
elif op == '*':
    result = x * y
elif op == '/':
    result = x / y

print("* " * 10)
print("{0} {1} {2} = {3}".format(x, op, y, result))
print("* " * 10)
