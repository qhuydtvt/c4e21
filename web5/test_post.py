import mlab
from post import Post

#1. Connect
mlab.connect()

# #2. Create data
# p = Post(title="C4E21", author="Quan", content="Sap den project roi", likes=15)
# print(p.title)
# print(p.content)
# print(p.likes)
# print(p.author)

# #3. Write data
# p.save()

def test_load_data():
  #2. Load all documents
  all_posts = Post.objects() # lazy loading

  #3. Print all documents
  for post in all_posts:
    print(post.title)
    print(post.content)
    print(post.author)
    print("--------------")

def test_load_one_data(post_id):
  post = Post.objects().with_id(post_id) #None
  if post is None:
    print("Not found")
  else:
    print(post.title)
    print(post.author)
    print(post.content)

def delete_one_data(post_id):
  #1. Retrive document
  post = Post.objects().with_id(post_id)

  #2 Delete document
  if post is None:
    print("Post not found")
  else:
    post.delete()
  
def update_one(post_id, new_title):
  #1. Retrive post
  post = Post.objects().with_id(post_id)

  #2. Update
  # Slug
  post.update(set__title=new_title)

update_one("5b9cd23813389f1b445b5eba", "Riven thần kiếm")