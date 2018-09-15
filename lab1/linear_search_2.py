items = [4, 6, 78, -90, 78, 67, 100]
x = int(input("Enter a number: "))

if x in items:
    print("Found")
    found_index = items.index(x)
    print(found_index)
else:
    print("Not found")