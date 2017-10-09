import os
import datetime
fileLocation = str(os.path.dirname(os.path.abspath(__file__)) + '\errorFile.txt')

def onStart():
    try:
        target = open(fileLocation, 'r')
        back = target.read()
        target.close()
        target.open(fileLocation, 'w')
        target.truncate()
        target.write(back + "\n")
        target.write("Cur Session: " + str(datetime.datetime.now().time()))
    except Exception:
        target = open(fileLocation, 'w+')
        target.write("Cur Session: " + str(datetime.datetime.now().time()))
        target.close()

def error(message):
    target = open(fileLocation, 'r')
    back = target.read()
    target.close()
    target = open(fileLocation, 'w')
    target.write(str(back) + "\n")
    target.write(str(message))
    target.close()
