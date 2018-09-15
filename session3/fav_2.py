favs = ['netflix', 'teaching', 'rebull']
for i, item in enumerate(favs):
    print(i + 1, item)

while True:
    command = input("What you you want (C, R, U, D)?")
    if command == "C":
        new_item = input("Item to add?")
        favs.append(new_item)
        for i, item in enumerate(favs):
            print(i + 1, item)
    elif command == "R":
        for i, item in enumerate(favs):
            print(i + 1, item)
    elif command == "U":
        position = int(input("Position to update? "))
        item = input("Replacing item? ")
        favs[position - 1] = item
        for i, item in enumerate(favs):
                print(i + 1, item)
    elif command == "D":
        position = int(input("Position to delete? "))
        favs.pop(position - 1)
