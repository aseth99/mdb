import json
import pymongo 

#INSTEAD OF THIS FILE i just renamed the file from .txt to .json lolz

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["news"]

mycol = mydb["hammerNews"]

#inserted once.. only run this file once, or comment this section out if u fina run again
newsArr = []
jsonFileToBeOpened = "news.json"
txtFileName = "hammerNews2.json"

# for line in open(jsonFileToBeOpened, 'r'):
#     tweets.append(json.loads(line))
# jsonFileToBeOpened = "user_timeline_DutchNewsNL.json"
# for line in open(jsonFileToBeOpened, 'r'):
#     tweets.append(json.loads(line))
# with open(txtFileName, 'r') as the_file:
# 	for line in the_file:
# 		newsArr.append(line)
for line in open(txtFileName, 'r'):
	readableLine = r line
    newsArr.append(json.loads(line))

new_result = mycol.insert_many(newsArr)

#using regex all queries with text starting A
myquery = { "text": { "$regex": "^A" } }

mydoc = mycol.find(myquery,{ "_id": 1, "created_at": 1, "text": 1 })

for x in mydoc:
	print(x)