from sys import argv
import Parser
import ErrorHan

filename = "importantFile.txt"

toPrint = Parser.parseFile(filename)
print (str(toPrint))
