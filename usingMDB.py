import json
import pymongo 


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["oilersTest"]

mycol = mydb["oilersTweets"]

# client = MongoClient()
# db = client.oilersTest

# posts = mydb.posts

# post_data = {"created_at": "Wed Nov 28 05:45:09 +0000 2018", "text": "RT @Robin_Brownlee: How is the official supposed to see white ice between the back of the goal line and the front of the puck when he has h\u2026","name": "Lowetide", "screen_name": "Lowetide"}
# result = posts.insert_one(post_data)

# test = mycol.insert_one(post_data)

# print(test.inserted_id)

# tweet1 = {"_id": "1","created_at": "Wed Nov 28 04:55:37 +0000 2018", "text": "In Sweden, \"shiddhay\" means not quite right, a little off. It's pronounced much like the musical artist Sade pronou\u2026 https://t.co/I6euROYPES", "name": "Lowetide", "screen_name": "Lowetide"}
# tweet2 = {"created_at": "Wed Nov 28 04:05:43 +0000 2018", "text": "RT @TPS_Guy: Trey Fix-Wolanksy has 195 career points as an @EdmOilKings, that's 6th all-time for the franchise (current edition). When he h\u2026", "name": "Lowetide", "screen_name": "Lowetide"}
# tweet3 = {"created_at": "Wed Nov 28 03:35:26 +0000 2018", "text": "@revRecluse Browns fans deserve a long, long run of success. Playoffs next year!","name": "Lowetide", "screen_name": "Lowetide"}

# new_result = mycol.insert_many([tweet1, tweet2, tweet3])
# print(new_result.inserted_ids)

#find all
# for x in mycol.find():
#   print(x)

#print all, print the created & text portions, not id
# for x in mycol.find({},{ "_id": 0, "created_at": 1, "text": 1 }):
#   print(x)

#print everythign cept text
# for x in mycol.find({},{ "text": 0 }):
#   print(x)

#print texts with id = 1
# myquery = { "_id": "1" }

# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)

#all queries with text starting with greater than RT
# myquery = { "text": { "$gt": "RT" } }

# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)

#using regex, find queriest starting with In
# myquery = { "text": { "$regex": "^In" } }

# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)

#sorting
# mydoc = mycol.find().sort("text")

# for x in mydoc:
#   print(x)
# mydoc = mycol.find().sort("text", -1)

# for x in mydoc:
#   print(x)
#deleting one
# myquery = { "text": { "$regex": "^In" } }

# mycol.delete_one(myquery)

#delete many
# myquery = { "text": {"$regex": "^In"} }

# x = mycol.delete_many(myquery)

# print(x.deleted_count, " documents deleted.")

#delete all docs in a collection
# x = mycol.delete_many({})

#delete collection
# mycol.drop()
# print(x.deleted_count, " documents deleted.")


#update collection
# myquery = { "text": {"$regex": "^In"} }
# newvalues = { "$set": { "text": "Canyon 123" } }


#update many
# myquery = { "address": { "$regex": "^S" } }
# newvalues = { "$set": { "name": "Minnie" } }

# x = mycol.update_many(myquery, newvalues)

# print(x.modified_count, "documents updated.")

#limit result
# myresult = mycol.find().limit(2)

# #print the result:
# for x in myresult:
#   print(x)



# mycol.update_one(myquery, newvalues)

#print "customers" after the update:
# for x in mycol.find():
#   print(x)


# print('One post: {0}'.format(result.inserted_id))

# print('Multiple posts: {0}'.format(new_result.inserted_ids))


# 


# oilersTweets = mydb.tweets

# for line in open('user_timeline_Lowetide.json', 'r'):
#         oilersTweets.insert(json.loads(line))
# for line in open('user_timeline_OilersNation.json', 'r'):
#         oilersTweets.insert(json.loads(line))
# for line in open('user_timeline_JasonGregor.json', 'r'):
#         oilersTweets.insert(json.loads(line))
# for line in open('user_timeline_Robin_Brownlee.json', 'r'):
#         oilersTweets.insert(json.loads(line))
# for line in open('user_timeline_SportsnetSpec.json', 'r'):
#         oilersTweets.insert(json.loads(line))
# for line in open('user_timeline_dstaples.json', 'r'):
#         oilersTweets.insert(json.loads(line))

# cursor = mydb.oilersTest.find({"created_at": "Wed Nov 28 05:45:09 +0000 2018"})
# dblist = myclient.list_database_names()
# if "mydatabase" in dblist:
#   print("The database exists.")
print(mydb.list_collection_names())

collist = mydb.list_collection_names()
if "oilersTweets" in collist:
  print("The collection exists.")

# print(cursor)

myclient.close()
