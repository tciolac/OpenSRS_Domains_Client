import os
from datetime import datetime

currTime = datetime.utcnow()
timeList = str(currTime).split(' ')
time = timeList[1][:-7]
dateList = str(timeList[0]).split('-')
parentFolder = "logs/" + dateList[0]
childFolder = "logs/" + dateList[0] + "/" + dateList[0] + "-" + dateList[1] + "-" + dateList[2]
apiServices = ['apiOpenSRS' , 'apiTestOpenSRS']

def maker():
	if not os.path.isdir(parentFolder):
		os.makedirs(parentFolder)
	if not os.path.isdir(childFolder):
		os.makedirs(childFolder)
	counter = 0
	while len(apiServices) > counter:
		if not os.path.isfile(childFolder + "/" + apiServices[(counter)] + ".log"):
			open(childFolder + "/" + apiServices[(counter)] + ".log","w+", encoding="utf-8")
		counter = counter + 1

def logEvent(event,service):
	with open(childFolder + "/" + apiServices[(service)] + ".log", 'a', encoding="utf-8") as currFile:
		currFile.write(str(currTime)[:-7] + ' | ' + str(event).replace("\n", "").replace("    ", "").replace("   ","").replace("  ","").replace("> <","><") + "\n")

maker()