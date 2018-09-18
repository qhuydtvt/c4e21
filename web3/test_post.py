import mlab
from post import Post

#1. Connect
mlab.connect()

#2. Create data
p = Post(title="C4E21", author="Quan", content="Sap den project roi", likes=15)
print(p.title)
print(p.content)
print(p.likes)
print(p.author)

#3. Write data
p.save()
