def parseFile(fileName):
    extracted = []
    if fileName.endswith(".java") or fileName.endswith(".txt"):
        with open(fileName) as target:
            for i in target:
                extracted.append(str(i))
        print (type(extracted))
        return extracted
    else:
        print ("Sorry that is not a valid file Type")
        return 0
knownTypes = ["int", "double", "String", "float"]

def getDataTypes(data):
    if type(data) is not 'list':
        print ("")
