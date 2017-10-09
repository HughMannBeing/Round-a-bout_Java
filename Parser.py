import ErrorHan

def parseFile(fileName):
    extracted = []
    if fileName.endswith(".java") or fileName.endswith(".txt"):
        with open(fileName) as target:
            for i in target:
                extracted.append(str(i))
        return extracted
    else:
        print ("Sorry that is not a valid file Type")
        return 0

knownTypes = ["int", "double", "String", "float"]
badChars = ["\\n"]

def getDataTypes(data):
    currentTypes = {}
    if type(data) is not 'list':
        ErrorHan.error("Passed value is not a list")
    else:
        for i in data:
            #i = cleanString(i)
            if knownTypes in i:
                store = i.split()
                varType = None
                varName = None
                for l in store:
                    if l in knownTypes:
                        varType = findType(l)
                    elif len(l) > 0:
                        varName = l
                currentTypes[varName] = varType
    print (currentTypes)

def cleanString(inData):
    dent = list(inData)
    finalArray = []
    finalString = ""
    for i in range(0, len(dent)):
        if str(dent)[i : i + 1] == "\\n":
            print ("Caught bad char")
            pass
        else:
            finalArray.append(dent[i])
    print (finalString.join(str(finalArray)))


def findType(key):
    for cur in knownTypes:
        if cur == key:
            return cur
