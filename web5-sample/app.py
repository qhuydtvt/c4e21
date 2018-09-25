from flask import Flask, render_template, request, redirect, url_for
import mlab
from post import Post

app = Flask(__name__)
mlab.connect()

@app.route("/post/<post_id>")
def post(post_id):
  post = Post.objects().with_id(post_id)
  return render_template("post.html", post=post)

@app.route("/delete/<post_id>")
def delete_post(post_id):
  post = Post.objects().with_id(post_id)
  if post is None:
    return "Not found"
  else:
    post.delete()
    return "Deleted"

@app.route("/update/<post_id>", methods=["GET", "POST"])
def update(post_id):
  p = Post.objects().with_id(post_id)
  #try - except
  if p is None:
    return "Not found"
  else:
    # GET
    if request.method == "GET":
      return render_template("update_post.html", post=p)
    elif request.method == "POST":
      # 1. Extract form
      form = request.form
      title = form['title']
      author = form['author']
      content = form['content']

      # 2. Update data
      # inc__likes
      # push__
      p.update(set__title=title, set__author=author, set__content=content)
      #p.reload()
      return redirect("/posts")

@app.route("/posts")
def posts():
  all_posts = Post.objects()
  return render_template("posts.html", posts=all_posts)


@app.route("/new-post", methods=["GET", "POST"])
def new_post():
  if request.method == "GET":
    return render_template("new_post.html")
  elif request.method == "POST":
    # 1. Get form & extract data
    form = request.form
    t = form["title"]
    a = form["author"]
    c = form["content"]
    
    # 2. Add new post
    new_post = Post(title=t, author=a, content=c)
    new_post.save()

    return redirect(url_for("posts"))

if __name__ == "__main__":
  app.run(debug=True)

