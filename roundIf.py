def getCondition(data):
    #This should just take the base definition line of the if statement
    #In the form: if (cond) {}
    foundCondition = ""
    dent = list(data)
    mark = False
    startPosition = 0
    curPosition = 0
    for i in dent:
        if i == "(":
            mark = True
            startPosition = curPosition
        elif i == ")":
            return foundCondition
        elif mark == True:
            foundCondition += str(i)
        curPosition += 1;

def roundToIf(condition):
    print ("if (Boolean.toString(" + str(condition) + ")).equals(\"true\")")
