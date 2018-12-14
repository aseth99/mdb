# mdb
fiddling around with and learning mongodb (using with python --> pymongo)


go to https://cloud.mongodb.com

log in
go to cluster-->security & add your username & add IP to whitelist if you havent already

connect to mongo shell:

mongo "mongodb://documents-shard-00-00-oz2kh.azure.mongodb.net:27017,documents-shard-00-01-oz2kh.azure.mongodb.net:27017,documents-shard-00-02-oz2kh.azure.mongodb.net:27017/test?replicaSet=documents-shard-0" --ssl --authenticationDatabase admin --username <USERNAME> --password <PASSWORD>
  
  
import data from json file (path to file too):
mongoimport --host documents-shard-0/documents-shard-00-00-oz2kh.azure.mongodb.net:27017,documents-shard-00-01-oz2kh.azure.mongodb.net:27017,documents-shard-00-02-oz2kh.azure.mongodb.net:27017 --ssl --username <USERNAME> --password <PASSWORD> --authenticationDatabase admin --db <DATABASE> --collection <COLLECTION> --type <FILETYPE> --file <FILENAME>
