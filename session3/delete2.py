favs = ['netflix', 'quora', 'teaching']

for i, fav in enumerate(favs):
    print(i + 1, '. ', fav, sep='')
print("* " * 20)

f = input("Enter favorite to delete? ")

if f in favs:
    favs.remove(f)
else:
    print("Nah")

for i, fav in enumerate(favs):
    print(i + 1, '. ', fav, sep='')
print("* " * 20)
