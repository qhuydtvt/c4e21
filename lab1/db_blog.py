# 1. Connect to database
from pymongo import MongoClient
from bson.objectid import ObjectId

uri = "mongodb://admin:codethechange18@ds235352.mlab.com:35352/c4e21"

client = MongoClient(uri)
db = client.get_default_database()

# 2. Select collection
posts = db["posts"]

# 3. Create document
post = {
    "title": "Hôm nay trời nắng",
    "content": "Tôi vẫn đi học code",
}

# 4. Insert document
posts.insert_one(post)

# print("Done")

post_list = posts.find()
# for post in post_list: # post_list ~ collection ~ list
#     print(post) # post ~ document ~ dictionary
cond = {
    "title": {
        "$regex": "hôm nay",
        "$options": "i",
    }
}

post = posts.find_one(cond)
print(post)
