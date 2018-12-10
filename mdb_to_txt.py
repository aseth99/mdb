import pymongo 


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["news"]

mycol = mydb["newsTweets"]

txtFileName = "testData.txt"


for x in mycol.find({},{ "_id": 0, "text": 1 }):
  print(x)
  textData = x.get('text')
  with open(txtFileName, 'a') as the_file:
  	the_file.write(textData+"\n")





#use regex like dis, find queriest starting with In
# myquery = { "text": { "$regex": "^In" } }

# mydoc = mycol.find(myquery)
