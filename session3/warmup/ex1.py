# print('''x x x x
# x x x x
# x x x x''')
n = int(input("n = ?"))
m = int(input("m = ?"))
for i in range(n):
    for j in range(m):
        print("x ", end="")
    print()