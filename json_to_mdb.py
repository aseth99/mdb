import json
import pymongo 


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["oilersTest"]

mycol = mydb["oilersTweets"]

#inserted once.. only run this file once, or comment this section out if u fina run again
tweets = []
jsonFileToBeOpened = "user_timeline_OilersNation.json"
for line in open(jsonFileToBeOpened, 'r'):
    tweets.append(json.loads(line))

new_result = mycol.insert_many(tweets)

#using regex all queries with text starting RT
myquery = { "text": { "$regex": "^RT" } }

mydoc = mycol.find(myquery,{ "_id": 0, "created_at": 1, "text": 1 })

for x in mydoc:
  print(x)