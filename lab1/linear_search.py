items = [8, 9, 10, -1, 23, 45, 99, -76]

x = int(input("Enter a number: "))

for index, item in enumerate(items):
    if x == item:
        print("Found it")
        print(index)
        break # find one
else:
    print("Not found")