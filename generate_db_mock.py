
import os
import json
from datetime import datetime


def generateDbMock():
    mockFile = open('mockfile.json', 'w+')
    objectList = []

    for i in range(1, 20):
        object = {
            "name": "Item#" + str(i),
            "description": "desc#" + str(i),
            "price": i * 10,
            "quantity": 100,
            "active": 1,
            "register_date": datetime.now().strftime('%Y-%m-%d'),
            "update_date": datetime.now().strftime('%Y-%m-%d'),
        }
        objectList.append(object)

    mockFile.write(json.dumps(objectList))
    mockFile.close()


def changeMockFileName(oldName, newName):
    if os.path.exists(oldName):
        os.rename(oldName, newName)

def deleteMockFile(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)

# generateDbMock()
# deleteMockFile('mockfile.json')
# changeMockFileName('db_mock_file.json', 'db_mock.json')

