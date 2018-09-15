fav_items = ['neflix', 'quora', 'medium', 'redbull']

while True:
    command = input("What do you want (C, R, U, D) ?").upper()
    if command == "C":
        new_item = input("New item? ")
        fav_items.append(new_item)
        print(fav_items)
    elif command == "R":
        for i, item in  enumerate(fav_items):
            print(i, item)  