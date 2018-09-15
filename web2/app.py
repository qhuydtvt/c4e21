from flask import Flask, render_template
app = Flask(__name__)

p = {
  "title": "C4E21",
  "content": "Module web, sắp hackathon",
  "author": "Quân",
  "date": "2018/09/02",
}

ps = [
  {
    "title": "C4E21",
    "content": "Module web, sắp hackathon",
    "author": "Quân",
    "date": "2018/09/02",
  },
  {
    "title": "C4E21 - Hackathon",
    "content": "8 giờ code, hoàn thiện sản phẩm",
    "author": "Huy",
    "date": "2018/09/03",
  },
  {
    "title": "C4E21 - Demo",
    "content": "2 phút trình bày, 15 phút hỏi đáp, sản phẩm sẵn sàng",
    "author": "Mạnh",
    "date": "2018/09/04",
  }
]

@app.route("/dict")
def one_dict():
  return render_template("dict.html", post=p)


@app.route("/dicts")
def many_dicts():
  return render_template("dicts.html", posts=ps)


if __name__ == "__main__":
  app.run(debug=True)