#1. Create a flask app
from flask import Flask, render_template

app = Flask(__name__)

ps = [
    "On July 16, 1969, the Apollo 11 spacecraft launched from the Kennedy Space Center in Florida. Its mission was to go where no human being had gone before—the moon! The crew consisted of Neil Armstrong, Michael Collins, and Buzz Aldrin. The spacecraft landed on the moon in the Sea of Tranquility, a basaltic flood plain, on July 20, 1969. The moonwalk took place the following day. On July 21, 1969, at precisely 10:56 EDT, Commander Neil Armstrong emerged from the Lunar Module and took his famous first step onto the moon’s surface. He declared, “That’s one small step for man, one giant leap for mankind.” It was a monumental moment in human history!",
    "Here is the perfect system for cleaning your room. First, move all of the items that do not have a proper place to the center of the room. Get rid of at least five things that you have not used within the last year. Take out all of the trash, and place all of the dirty dishes in the kitchen sink. Now find a location for each of the items you had placed in the center of the room. For any remaining items, see if you can squeeze them in under your bed or stuff them into the back of your closet. See, that was easy!",
    "The Blue Whales just played their first baseball game of the new season; I believe there is much to be excited about. Although they lost, it was against an excellent team that had won the championship last year. The Blue Whales fell behind early but showed excellent teamwork and came back to tie the game. The team had 15 hits and scored 8 runs. That’s excellent! Unfortunately, they had 5 fielding errors, which kept the other team in the lead the entire game. The game ended with the umpire making a bad call, and if the call had gone the other way, the Blue Whales might have actually won the game. It wasn’t a victory, but I say the Blue Whales look like they have a shot at the championship, especially if they continue to improve.",
  ]

@app.route("/posts")
def posts():
  shortened_ps = []
  for post in ps:
    shortened_ps.append(post[0:40])
  
  return render_template("post_list.html",
          posts=shortened_ps)

@app.route("/posts/<int:position>")
def post_detail(position):
  if position < 0 or position >= len(ps):
    return "Not found", 404
  post = ps[position - 1]
  return render_template("post_detail.html", post=post)


#2. Create router
@app.route("/")
def homepage():
  return render_template("homepage.html", 
    title="Ca dao về sen",
    posts=ps)

@app.route("/huy")
def hello_huy():
  return "Hello Huy"

@app.route("/hello/<name>")
def hello(name):
  return "Hello " + name

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
  result = a + b
  return str(result)


@app.route("/h1tag")
def h1tag():
  return "<h1>Heading 1 - Bigggg</h1><p>Hom nay toi buon</p>"


#3 Run app
print("Running app")
if __name__ == "__main__":
  app.run(debug=True) # listening