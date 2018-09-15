favs = ['netflix', 'teaching', 'quora']

for i, fav in enumerate(favs):
    print(i + 1, '. ', fav, sep='')
print("* " * 20)

position = int(input("Position to delete? "))
favs.pop(position - 1)

for i, fav in enumerate(favs):
    print(i + 1, '. ', fav, sep='')
print("* " * 20)