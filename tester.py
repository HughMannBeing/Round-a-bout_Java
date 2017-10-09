from sys import argv
import Parser
import ErrorHan
import roundIf

script, filename = argv

#bigString = "if ( x == 1 )"
#roundIf.roundToIf(roundIf.getCondition(bigString))

gotData = Parser.parseFile(filename)
for i in gotData:
    print (i)
