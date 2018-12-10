import json
 


txtFileName = "testData.txt"

tweets = []

jsonFileToBeOpened = "user_timeline_dutchdailynews.json"
for line in open(jsonFileToBeOpened, 'r'):
    tweets.append(json.loads(line))
jsonFileToBeOpened = "user_timeline_DutchNewsNL.json"
for line in open(jsonFileToBeOpened, 'r'):
    tweets.append(json.loads(line))

for line in tweets:
    textData = line.get('text')

    with open(txtFileName, 'a') as the_file:
        the_file.write(textData+"\n")


