import json
 

#TEXT HAS QUOTES IN IT, THUS LEADS TO ERROR

txtFileName = "hammerNews.txt"
newsArr = []

jsonFileToBeOpened = "news.json"
for line in open(jsonFileToBeOpened, 'r'):
    newsArr.append(json.loads(line))
# jsonFileToBeOpened = "user_timeline_DutchNewsNL.json"
# for line in open(jsonFileToBeOpened, 'r'):
#     tweets.append(json.loads(line))
count = 1
for line in newsArr:
	idData = count
	idLine = "{" + "\"id\":\"{}\", ".format(idData)
	textData = line.get('text')
	textLine = "\"text\":\"{}\", ".format(textData)
	urlData = line.get('url')
	urlLine = "\"url\":\"{}\", ".format(urlData)
	publicationdateData = line.get('publication date')
	publicationdateLine = "\"publication date\":\"{}\", ".format(publicationdateData)
	sourceData = line.get('source')
	sourceLine = "\"source\": \"{}\"".format(sourceData) + "}"
	count = count + 1



	dictText = idLine + textLine + urlLine + publicationdateLine + sourceLine
	print(dictText)
	# with open(filename, 'wb') as outfile:
	# 	json.dump(dictData, outfile)
	
	with open(txtFileName, 'a') as the_file:
		the_file.write(dictText + "\n")


