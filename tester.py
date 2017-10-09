from sys import argv
import Parser
import ErrorHan

fileName = "importantFile.txt"

toPrint = Parser.getDataTypes(Parser.parseFile(fileName))
print (toPrint)
