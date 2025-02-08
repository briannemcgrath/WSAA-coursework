import requests
import csv
from xml.dom.minidom import parseString

retrieveTags=['TrainStatus',
              'TrainLatitude',
              'TrainLongitude',
              'TrainCode',
              'PublicMessage',
              'Direction'
              ]


#fetch XML Data
url ="https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML" #API URL
page = requests.get(url)
doc = parseString(page.content)

#checking XML content - comment out once works
#print (doc.toprettyxml())

#saving xml to a file in the lab directory
with open ("labs/trainxml.xml", "w") as xmlfp:
    doc.writexml(xmlfp)

#extract and print train codes
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")

for objTrainPositionsNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    traincode = traincodenode.firstChild.nodeValue.strip()
    #print(traincode)

#extract and store train codes in csv
with open("labs/trains.csv", mode="w", newline="") as train_file:
    train_writer = csv.writer(train_file)

    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        train_writer.writerow([traincode])