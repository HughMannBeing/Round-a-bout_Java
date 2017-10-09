from sys import argv
import Parser
import ErrorHan

filename = "importantFile.txt"

ErrorHan.onStart()
ErrorHan.error("Butts")

toPrint = Parser.parseFile(filename)
print (str(toPrint))
