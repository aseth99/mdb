#doesnt work idk went another route
import json
 


txtFileName = "hammerNews.txt"
filename = "news2.json"
newsArr = []

jsonFileToBeOpened = "news.json"
for line in open(jsonFileToBeOpened, 'r'):
    newsArr.append(json.loads(line))
# jsonFileToBeOpened = "user_timeline_DutchNewsNL.json"
# for line in open(jsonFileToBeOpened, 'r'):
#     tweets.append(json.loads(line))
count = 1
for line in newsArr:
	dictData = {}
	idData = count
	textData = line.get('text')
	urlData = line.get('url')
	publicationdateData = line.get('publication date')
	sourceData = line.get('source')

	dictData.update({"id":idData,"text":textData,"source": sourceData,"publication date": publicationdateData})


	with open(filename, 'wb') as outfile:
		json.dump(dictData, outfile)
	
	# ith open(txtFileName, 'a') as the_file:
	# 	the_file.write(dictData)
	# 	the_file.write("\n")


