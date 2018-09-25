from mongoengine import Document, StringField, IntField

class Post(Document):
  meta = {'strict': False}
  title = StringField()
  author = StringField()
  content = StringField()
  image = StringField()
  likes = IntField(default=0)
